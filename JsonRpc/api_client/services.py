import json
import os
import ssl
import urllib.request

from django.conf import settings


class SSLContextFactory:
    @staticmethod
    def create_ssl_context():
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        with open("temp_cert.pem", "w") as cert_file:
            cert_file.write(settings.CRT)

        with open("temp_key.pem", "w") as key_file:
            key_file.write(settings.KEY)

        context.load_cert_chain(certfile="temp_cert.pem", keyfile="temp_key.pem")
        os.remove("temp_cert.pem")
        os.remove("temp_key.pem")
        return context


class JsonRpcClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def call_api_method(self, method, params=None):
        params = params or []
        payload = {"jsonrpc": "2.0", "method": method, "params": params, "id": 1}
        ssl_context = SSLContextFactory.create_ssl_context()
        req = urllib.request.Request(
            self.endpoint, data=json.dumps(payload).encode("utf-8"), headers={"Content-type": "application/json"}
        )
        with urllib.request.urlopen(req, context=ssl_context) as response:
            response_data = response.read()
            json_response = json.loads(response_data)
            return json_response
