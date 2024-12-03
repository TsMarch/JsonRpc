# Generated by Django 5.1.3 on 2024-12-03 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ErrorLog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("method_name", models.CharField(max_length=255)),
                ("params", models.JSONField()),
                ("error_message", models.TextField()),
                ("occurred_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]