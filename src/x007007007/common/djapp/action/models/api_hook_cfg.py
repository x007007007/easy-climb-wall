from .cfg_base import CfgModelBase
from django.db import models
from django.template import Template, Context


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

    def run_action(self, config):
        import requests
        kwargs = {}
        if self.header:
            kwargs['header'] = self.header
        if self.body_template:
            template = Template(self.body_template)
            res = template.render(Context(config))
            kwargs['data'] = res
        requests.Request(
            url=self.url,
            method=self.method,
            **kwargs,
        )
        return True