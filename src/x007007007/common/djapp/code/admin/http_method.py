from ..models import HttpMethod
from django.contrib import admin

@admin.register(HttpMethod)
class HttpMethodAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )