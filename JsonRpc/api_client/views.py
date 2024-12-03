import json

from django.shortcuts import render
from error_handler.views import log_error
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import JsonRpcClient


class JsonRpcView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "form.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        method = request.data.get("method")
        params = request.data.get("params", "")
        endpoint = request.data.get("endpoint", "https://slb.medv.ru/api/v2/")
        params = json.loads(params) if params else []
        client = JsonRpcClient(endpoint)
        response = client.call_api_method(method, params)
        if response.get("error"):
            log_error(method_name=method, params=params, error_message=response.get("error"))
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return render(request, self.template_name, {"result": response})
