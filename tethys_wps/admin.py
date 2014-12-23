from django.contrib import admin
from .models import WebProcessingService


class WebProcessingServiceAdmin(admin.ModelAdmin):
    """
    Admin model for Web Processing Service Model
    """
    fields = ('name', 'endpoint', 'username', 'password')



admin.site.register(WebProcessingService, WebProcessingServiceAdmin)
