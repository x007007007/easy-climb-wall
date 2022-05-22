from django.db import models
import logging

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


logger = logging.getLogger(__name__)


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

    action_retry = models.IntegerField(default=3)
    action_retry_interval = models.IntegerField(default=60)

    class Meta:
        unique_together = (
            ('config_type', 'config_id'),
        )

    @property
    def get_config(self):
        return f"{self.config}"

    def run_action(self, config):
        logger.debug(f"run action ref {self.id}: {config}")
        if self.enable:
            return self.config.run_action(config)