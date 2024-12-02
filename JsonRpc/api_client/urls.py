from django.urls import include, path
from rest_framework import routers

from .views import JsonRpcView

urlpatterns = [path("api_view/", JsonRpcView.as_view())]
