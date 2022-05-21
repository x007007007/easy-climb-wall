from django.contrib import admin

from ..models import StatusChangeLogModel


@admin.register(StatusChangeLogModel)
class StatusChangeLogModelAdmin(admin.ModelAdmin):
    search_fields = (
        'process__template__name',
        'status_name',
    )
    list_display = (
        'id',
        'process',
        'status',
        'status_name',
        'created_time',
    )
    list_filter = (
        'status',
        'process__template__name',
    )
