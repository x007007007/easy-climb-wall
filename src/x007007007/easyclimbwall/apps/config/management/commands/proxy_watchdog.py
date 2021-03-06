import os
import warnings

from django.core.management.base import BaseCommand, CommandError
from x007007007.easyclimbwall.apps.config.models import ProxyConfigModel
import time



class Command(BaseCommand):

    def handle(self, *args, **options):
        while True:
            time.sleep(300)
            self.deal()

    def deal(self):
        status_change = False
        for config in ProxyConfigModel.objects.filter():  # type: ProxyConfigModel
            assert isinstance(config, ProxyConfigModel)
            if not config.enabled and config.read_pid():
                config.stop_server()
                status_change = True
            elif config.enabled and not config.read_pid():
                config.start_server()
                status_change = True
        if status_change:
            ProxyConfigModel.update_service_label()

