from django.contrib import admin
from ..models import ReferModel


@admin.register(ReferModel)
class ReferModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'config_type',
        'config_id',
        'enable',
        'config',
    )



