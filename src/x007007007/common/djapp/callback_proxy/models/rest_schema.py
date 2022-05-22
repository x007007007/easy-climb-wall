import inspect

from django.db import models
from rest_framework import serializers
# Create your models here.


def get_serializer_list():
    res = []
    for n in dir(serializers):
        if e := getattr(serializers, n, None):
            if inspect.isclass(e) and issubclass(e, serializers.Field):
                res.append((n, n))
    return res


class ConfigAPISchemaItem(models.Model):
    name = models.CharField(max_length=254,)
    type = models.CharField(max_length=64, choices=get_serializer_list())
    config = models.ForeignKey("ConfigModel", on_delete=models.CASCADE)
    extra = models.JSONField(default=dict, blank=True, null=True)