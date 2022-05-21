from django.db import models


class StatusModel(models.Model):
    name = models.CharField(max_length=254)
    template = models.ForeignKey("TemplateModel", on_delete=models.CASCADE)

    next_status_set = models.ManyToManyField(
        through="AvailableNextStatusModel",
        to="StatusModel",
        related_name="pre_status_set"
    )
    is_finish_status = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"<{self.__class__.__name__}({self.id}) {self.name}>"
    