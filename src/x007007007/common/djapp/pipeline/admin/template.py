from django.contrib import admin

from ..models import TemplateModel

@admin.register(TemplateModel)
class TemplateModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )