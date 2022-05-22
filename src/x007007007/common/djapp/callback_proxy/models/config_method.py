from django.db import models


class ConfigMethodRel(models.Model):
    config = models.ForeignKey('ConfigModel', on_delete=models.CASCADE)
    method = models.ForeignKey('common_code.HttpMethod', on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            ('config', 'method'),
        )