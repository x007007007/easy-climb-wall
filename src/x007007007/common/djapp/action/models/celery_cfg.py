from .cfg_base import CfgModelBase
from django.db import models


class CeleryCfgModel(CfgModelBase):
    task_name = models.CharField(max_length=254)
    queue_name = models.CharField(max_length=254)
    broken_url = models.CharField(max_length=254)
    backend = models.CharField(max_length=254)
    task_args = models.JSONField()

    def run_action(self, config):
        import celery
        cclient = celery.Celery(
            'celery_action',
            broker=self.broken_url,
        )
        async_task = cclient.send_task(
            name=self.task_name, kwargs={
                'config': config
            }
        )
        return True