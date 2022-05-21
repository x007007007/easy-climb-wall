from .cfg_base import CfgModelBase
from django.db import models


class ApiHookCfgModel(CfgModelBase):
    url = models.CharField(max_length=254)
    method = models.CharField(
        choices=(
            ("HEAD", "HEAD"),
            ("GET", "GET"),
            ("POST", "POST"),
            ("DELETE", "DELETE"),
            ("PUT", "PUT"),
            ("PATCH", "PATCH"),
            ("OPTIONAL", "OPTIONAL"),
        ),
        max_length=8
    )
    header = models.JSONField(null=True, blank=True)
    body_template = models.TextField(null=True, blank=True, default=None)
