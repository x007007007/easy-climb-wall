from django.db import models


class ChangeStatusStrategyModel(models.Model):
    change_rule = models.ForeignKey("AvailableNextStatusModel", on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    sub_template = models.ForeignKey(
        "TemplateModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

