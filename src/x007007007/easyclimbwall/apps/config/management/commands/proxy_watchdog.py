import os
import warnings

from django.core.management.base import BaseCommand, CommandError
from x007007007.easyclimbwall.apps.config.models import ProxyConfigModel
from django.conf import settings
import time
import glob
import psutil



class Command(BaseCommand):

    def load_all_pid(self):
        remove_pid = []
        pid_list = []
        for file_name in glob.glob(f"{settings.SERVICE_PID_FOLDER}/*.pid"):
            with open(file_name) as fp:
                try:
                    pid = int(fp.read().strip())
                    psutil.Process(pid)
                except:
                    remove_pid.append(file_name)
                    os.remove(file_name)
            pid_list.append(pid)
        return pid_list


    def handle(self, *args, **options):
        while True:
            time.sleep(300)
            self.deal()

    def deal(self):
        for config in ProxyConfigModel.objects.filter():  # type: ProxyConfigModel
            if config.enabled:
                pass