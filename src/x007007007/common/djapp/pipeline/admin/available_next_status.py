from django.contrib import admin

from ..models import AvailableNextStatusModel


@admin.register(AvailableNextStatusModel)
class StatusModelAdmin(admin.ModelAdmin):
    list_display = (
        'src',
        'dst'
    )

