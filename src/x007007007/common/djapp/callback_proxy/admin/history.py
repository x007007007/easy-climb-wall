from django.contrib import admin
from ..models import ConfigModel, ConfigAPISchemaItem
from ..models import HistoryModel



@admin.register(HistoryModel)
class HistoryModelAdmin(admin.ModelAdmin):
    search_fields = (
        'request',
        'header',
    )
    list_display = (
        'config',
        'params',
        'request',
        'header',
        'created_time',
    )
    list_filter = (
        'config__name',
        'created_time',
    )

    def has_add_permission(self, request):
        return False

    def action_resend(self, request, queryset):
        for obj in queryset:
            assert isinstance(obj, HistoryModel)
            obj.send_task()

    actions = [
        'action_resend',
    ]