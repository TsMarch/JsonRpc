from django.test import TestCase

from .services import JsonRpcClient


class JsonRpcClientTests(TestCase):
    def test_auth(self):
        client = JsonRpcClient("https://slb.medv.ru/api/v2/")
        response = client.call_api_method("auth.check")

        self.assertIn("result", response)
        self.assertNotIn("error", response)
