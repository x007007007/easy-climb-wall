import celery
import logging
from django.db import models
from django.utils import timezone

logger = logging.getLogger(__name__)


class HistoryModel(models.Model):
    config = models.ForeignKey("ConfigModel", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    request = models.TextField()
    header = models.JSONField()
    params = models.TextField()

    def run_action(self):
        self.config.action.run_action(
            config={
                'header': self.header,
                'params': self.params,
                'data': self.request,
            }
        )