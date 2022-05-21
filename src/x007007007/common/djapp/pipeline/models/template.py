from django.db import models


class TemplateModel(models.Model):
    name = models.CharField(max_length=254)
    start_status = models.ForeignKey(
        "StatusModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    is_record_status_change_history = models.BooleanField(default=False)
    
    def __str__(self):
        return f"<{self.__class__.__name__} ({self.id}) {self.name}>"