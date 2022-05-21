from .cfg_base import CfgModelBase
from django.db import models


class CeleryCfgModel(CfgModelBase):
    task_name = models.CharField(max_length=254)
    queue_name = models.CharField(max_length=254)
    broken_url = models.CharField(max_length=254)
    backend = models.CharField(max_length=254)
    task_args = models.JSONField()
