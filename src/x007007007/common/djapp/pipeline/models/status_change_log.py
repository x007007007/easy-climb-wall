from django.db import models


class StatusChangeLogModel(models.Model):
    process = models.ForeignKey(
        "ProcessModel",
        on_delete=models.CASCADE
    )
    status = models.ForeignKey(
        'StatusModel',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    status_name = models.CharField(
        max_length=254,
    )
    created_time = models.DateTimeField(auto_now_add=True)

