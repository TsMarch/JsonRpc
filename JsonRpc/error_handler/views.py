from rest_framework.viewsets import ModelViewSet

from .models import ErrorLog
from .serializers import ErrorLogListSerializer


def log_error(method_name, params, error_message):
    ErrorLog.objects.create(method_name=method_name, params=params, error_message=error_message)


class ErrorViewSet(ModelViewSet):
    serializer_class = ErrorLogListSerializer
    queryset = ErrorLog.objects.all()
