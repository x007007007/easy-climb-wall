import warnings

from django.db import models
from .status_change_log import StatusChangeLogModel
from .status import StatusModel
from .available_next_status import AvailableNextStatusModel
from .change_status_action import ChangeStatusActionModel


class ProcessQuerySet(models.QuerySet):
    def change_status(self, status: StatusModel):
        for obj in self:
            assert isinstance(obj, ProcessModel)
            obj.current_status = status
            StatusChangeLogModel.objects.create(
                process=obj,
                status=status,
                status_name=status.name
            )
            obj.save()


class ProcessModel(models.Model):
    objects = ProcessQuerySet.as_manager()
    template = models.ForeignKey("TemplateModel", on_delete=models.CASCADE)

    current_status = models.ForeignKey(
        "StatusModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    change = models.ForeignKey(
        "AvailableNextStatusModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    change_action = models.ForeignKey(
        "ChangeStatusActionModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    parent = models.ForeignKey(
        "ProcessModel",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def change_status(self, status: StatusModel):
        if change_rule := self.current_status.dst_available_next_status_map_set.filter(dst=status).first():
            rows = self.__class__.objects.filter(
                id=self.id,
                change=self.change
            ).update(
                change=change_rule
            )
            self.refresh_from_db()
            assert self.change is not None
            if rows == 0:
                warnings.warn("database change")
                return False
            assert isinstance(self.change, AvailableNextStatusModel)
            change_action_list = list(self.change.changestatusactionmodel_set.filter(
                group=ChangeStatusActionModel.PRE_CHANGED
            ).order_by(
                'order',
            ).values())
            if self.change_action in change_action_list:
                offset = change_action_list.index(self.change_action)
            else:
                offset = 0
            for pre_action in change_action_list[offset:]:
                self.change_action = pre_action
                self.save(update_fields=('change_action',))
                if res := pre_action.run():
                    continue
                else:
                    break
            else:
                rows = self.__class__.objects.filter(
                    id=self.id,
                    current_status=self.current_status
                ).change_status(self.change.dst)
                if rows == 0:
                    warnings.warn("status change ")
                    return False
                for post_action in self.change.changestatusactionmodel_set.filter(
                    group=ChangeStatusActionModel.POST_CHANGED
                ).order_by(
                    'order',
                ):
                    self.change_action = post_action
                    self.save(update_fields=('change_action',))
                    post_action.run()
                self.change = None
                self.change_action = None
                self.save(update_fields=(
                    'change',
                    'change_action',
                ))
                return True
        return False
