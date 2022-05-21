from django.contrib import admin
from django.contrib import messages
from ..models import ProcessModel
from ..models import StatusModel
from django.contrib.admin.helpers import ActionForm
from django import forms


class StatusActionForm(ActionForm):
    status = forms.ModelChoiceField(queryset=StatusModel.objects.all())


@admin.register(ProcessModel)
class ProcessModelAdmin(admin.ModelAdmin):
    list_display = (
        'template',
        'current_status',
    )
    action_form = StatusActionForm

    def action_change_status(self, request, queryset):
        for obj in queryset:
            assert isinstance(obj, ProcessModel)
            if not obj.change_status(request.POST['status']):
                messages.error(message=f"{obj} change status failed", request=request)

    actions = [
        action_change_status
    ]