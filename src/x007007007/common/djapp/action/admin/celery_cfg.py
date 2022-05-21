from django.contrib import admin
from ..models import CeleryCfgModel


@admin.register(CeleryCfgModel)
class CeleryCfgModelAdmin(admin.ModelAdmin):
    list_filter = (
        'id',
        'name',
        'task_name',
        'queue_name',
        'backend',
    )