from django.contrib import admin

from ..models import ChangeStatusActionModel


@admin.register(ChangeStatusActionModel)
class ChangeStatusActionModelAdmin(admin.ModelAdmin):
    list_display = (
        'change_status',
        'action',
    )

