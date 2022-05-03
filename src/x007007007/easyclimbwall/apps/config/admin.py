from django.contrib import admin

# Register your models here.

from .models import ProxyConfigModel


@admin.register(ProxyConfigModel)
class ProxyConfigModelAdmin(admin.ModelAdmin):
    list_display = (
        'host',
        'path',
        'read_pid',
    )
    list_filter = (
        'enabled',
    )

    def action_start_service(self, request, queryset):
        for obj in queryset:
            assert isinstance(obj, ProxyConfigModel)
            obj.start_server()
        ProxyConfigModel.update_service_label()


    actions = [
        'action_start_service',
    ]