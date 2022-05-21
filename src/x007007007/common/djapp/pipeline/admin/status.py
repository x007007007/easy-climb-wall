from django.contrib import admin

from ..models import StatusModel


@admin.register(StatusModel)
class StatusModelAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )
    list_filter = (
        'template',
    )
    list_display = (
        'template',
        'name',
        'order',
    )
