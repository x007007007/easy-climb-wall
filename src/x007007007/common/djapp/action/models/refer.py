from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class ReferModel(models.Model):
    config_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={
            'model__endswith': 'cfgmodel',
        }
    )
    config_id = models.PositiveIntegerField()
    config = GenericForeignKey(
        'config_type',
        'config_id',
    )
    enable = models.BooleanField(default=True)

    class Meta:
        unique_together = (
            ('config_type', 'config_id'),
        )

    @property
    def get_config(self):
        return f"{self.config}"