from django.urls import include, path
from rest_framework import routers

from .views import ErrorViewSet

error_router = routers.DefaultRouter()
error_router.register("", ErrorViewSet, basename="errors")


urlpatterns = [
    path("", include(error_router.urls)),
]
