from django.contrib import admin
from django.shortcuts import reverse
from django.utils.safestring import mark_safe
# Register your models here.
from ..models import ConfigModel, ConfigAPISchemaItem
from x007007007.common.djapp.code.models import HttpMethod


class ConfigAPISchemaItemInline(admin.TabularInline):
    model = ConfigAPISchemaItem


class ConfigAllowMethodItemInline(admin.TabularInline):
    model = ConfigModel.allow_method_set.through


@admin.register(ConfigModel)
class ConfigModelAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )
    list_display = (
        'pk',
        'name',
        'action',
        'get_callback_url',
    )

    inlines = [
        ConfigAllowMethodItemInline,
        ConfigAPISchemaItemInline,
    ]

    def get_callback_url(self, obj):
        url_path = reverse("user-callback-url", kwargs=dict(
            postfix=obj.name
        ))
        return mark_safe(f"""
            <a href="{url_path}" target="_blank">{url_path}</a>
        """)


