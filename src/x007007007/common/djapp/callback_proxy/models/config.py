from django.db import models


class ConfigModel(models.Model):
    name = models.CharField(max_length=254)
    postfix_url = models.CharField(max_length=254,)
    allow_method = models.ManyToManyField(
        through='ConfigMethodRel',
        to='common_code.HttpMethod'
    )