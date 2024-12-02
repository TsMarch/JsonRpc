from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class JsonRpcView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "form.html"

    def post(self, request):
        method = request.data.get("method")
        params = request.data.get("params")
