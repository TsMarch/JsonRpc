import json

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from .services import JsonRpcClient, SSLContextFactory


class JsonRpcView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "form.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        method = request.data.get("method")
        params = request.data.get("params", '')
        params = json.loads(params) if params else []
        ssl_context = SSLContextFactory()
        client = JsonRpcClient("https://slb.medv.ru/api/v2/", ssl_context.create_ssl_context())

        try:
            response = client.call_api_method(method, params)
            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({'error': e}, status=500)
