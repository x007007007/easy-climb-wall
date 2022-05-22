from django.db import models


class ConfigModel(models.Model):
    name = models.CharField(max_length=254)
    postfix_url = models.CharField(max_length=254,)
    allow_method_set = models.ManyToManyField(
        through='ConfigMethodRel',
        to='common_code.HttpMethod'
    )
    action = models.ForeignKey(
        "common_action.ReferModel",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )