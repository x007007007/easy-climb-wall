from django.db import models


class ProcessModel(models.Model):
    template = models.ForeignKey("TemplateModel", on_delete=models.CASCADE)
    current_status = models.ForeignKey("StatusModel", on_delete=models.SET_NULL, null=True)

    parent = models.ForeignKey("ProcessModel", on_delete=models.CASCADE)

