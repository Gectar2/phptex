from django.contrib import admin
from .models import Technicalsupport
# Register your models here.

@admin.register(Technicalsupport)
class TechnicalsupportAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'messages', 'date_time']
    search_fields = ['name']
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
