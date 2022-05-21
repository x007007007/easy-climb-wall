from django.db import models


class ChangeStatusActionModel(models.Model):
    PRE_CHANGED = 'pre_changed'
    POST_CHANGED = 'post_changed'

    change_status = models.ForeignKey("AvailableNextStatusModel", on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    action = models.ForeignKey("common_action.ReferModel", on_delete=models.CASCADE)

    strategy = models.CharField(
        choices=(
            ('requisite', 'requisite'),  # 失败影响
            ('optional', 'optional'),  # 失败不影响是否往下跑
        ),
        max_length=16,
        default='optional',
    )
    group = models.CharField(
        choices=(
            (PRE_CHANGED, PRE_CHANGED),
            (POST_CHANGED, POST_CHANGED),
        ),
        max_length=16,
        default=POST_CHANGED
    )

    def run(self, **kwargs):
        return self.action.run_action(kwargs)

