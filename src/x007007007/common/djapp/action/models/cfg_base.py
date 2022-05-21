from django.db import models


class CfgModelBase(models.Model):
    name = models.CharField(max_length=254)
    action_func = models.CharField(max_length=254)

    class Meta:
        abstract = True