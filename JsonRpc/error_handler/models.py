from django.db import models


class ErrorLog(models.Model):
    method_name = models.CharField(max_length=255)
    params = models.JSONField()
    error_message = models.TextField()
    occurred_at = models.DateTimeField(auto_now_add=True)
