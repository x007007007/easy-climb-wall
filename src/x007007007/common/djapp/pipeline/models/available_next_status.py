from django.db import models


class AvailableNextStatusModel(models.Model):
    src = models.ForeignKey(
        "StatusModel",
        on_delete=models.CASCADE,
        related_name='dst_available_next_status_map_set'
    )
    dst = models.ForeignKey(
        "StatusModel",
        on_delete=models.CASCADE,
        related_name='src_available_next_status_map_set'
    )

    def __str__(self):
        return f"<{self.__class__.__name__} {self.id} {self.src} -> {self.dst}>"