from django.contrib import admin

from ..models import ChangeStatusStrategyModel


@admin.register(ChangeStatusStrategyModel)
class StatusModelAdmin(admin.ModelAdmin):
    list_display = (
        'change_rule',
        'sub_template'
    )

