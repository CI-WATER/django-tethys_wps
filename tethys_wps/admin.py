from django.contrib import admin
from .models import WebProcessingService
from django.forms import ModelForm, PasswordInput


class WebProcessingServiceForm(ModelForm):
    class Meta:
        model = WebProcessingService
        fields = ('name', 'endpoint', 'username', 'password')
        widgets = {
            'password': PasswordInput(),
        }


class WebProcessingServiceAdmin(admin.ModelAdmin):
    """
    Admin model for Web Processing Service Model
    """
    form = WebProcessingServiceForm
    fields = ('name', 'endpoint', 'username', 'password')



admin.site.register(WebProcessingService, WebProcessingServiceAdmin)
