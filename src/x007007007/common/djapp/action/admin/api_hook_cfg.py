from django.contrib import admin
from ..models import ApiHookCfgModel


@admin.register(ApiHookCfgModel)
class ApiHookCfgModelAdmin(admin.ModelAdmin):
    list_filter = (
        'id',
        'name',
        'url',
        'method',
    )