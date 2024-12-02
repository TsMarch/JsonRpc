import json
import ssl
import urllib.request


class JsonRpcClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def call_api_method(self, method, params=None):
        payload = {"jsonrpc": "2.0", "method": method, "params": params}
        pass
