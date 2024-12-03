from rest_framework import serializers

from .models import ErrorLog


class ErrorLogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorLog
        fields = "__all__"
