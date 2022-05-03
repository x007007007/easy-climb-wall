import json
import os.path

from django.db import models
# Create your models here.
from django.conf import settings
import psutil
import subprocess


class ProxyConfigModel(models.Model):
    comment = models.TextField(blank=True, default='')
    path = models.CharField(max_length=254)
    host = models.CharField(max_length=254)
    enabled = models.BooleanField(default=True)
    password = models.CharField(max_length=254)
    encryption = models.CharField(
        max_length=64,
    )
    timeout = models.PositiveIntegerField(default=20)
    pid = models.IntegerField(null=True, editable=False)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def read_pid(self):
        file_name = self.get_pid_file_path()
        if os.path.exists(file_name):
            with open(file_name) as fp:
                try:
                    pid = int(fp.read().strip())
                    psutil.Process(pid)
                except:
                    os.remove(file_name)
            return pid

    def get_pid_file_path(self):
        if not os.path.exists(f"{settings.SERVICE_PID_FOLDER}"):
            os.makedirs(settings.SERVICE_PID_FOLDER)
        return f"{settings.SERVICE_PID_FOLDER}/{self.pk}.pid"

    def get_config_path(self):
        if not os.path.exists(f"{settings.SERVICE_CONFIG_FOLDER}"):
            os.makedirs(settings.SERVICE_CONFIG_FOLDER)
        return os.path.join(settings.SERVICE_CONFIG_FOLDER, f"{self.pk}.conf")

    def get_server_port(self):
        return 10080 + self.pk

    def generate_config(self):
        with open(self.get_config_path(), "w") as fp:
            json.dump({
                "server": "0.0.0.0",
                "server_port": f"{self.get_server_port()}",
                "password": self.password,
                "timeout": self.timeout,
                "method": self.encryption,
                "plugin": "/usr/bin/v2ray-plugin",
                "plugin_opts": f"server;path={self.path}",
                "mode": "tcp_only",
                "reuse_port": True,
                "no_delay": True
            }, fp, indent=4)

    def start_server(self):
        config = self.get_config_path()
        cmds = [
            settings.SS_SERVER_CMD,
            "-c",
            self.get_config_path(),
            "-f",
            self.get_pid_file_path(),
            "-u"
        ]
        if not os.path.exists(config):
            self.generate_config()
        print(f"run: {cmds}")
        process = subprocess.Popen(cmds)