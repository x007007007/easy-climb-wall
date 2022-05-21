from django.db import models


class ChangeStatusActionModel(models.Model):
    change_status = models.ForeignKey("AvailableNextStatusModel", on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    action = models.ForeignKey("common_action.ReferModel", on_delete=models.CASCADE)
