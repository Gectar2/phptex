from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Addurlvet
# Register your models here.

class AddurlvetAdmin(SummernoteModelAdmin):
    list_display = ['name_link', 'name_page']
    summernote_fields = ('content_text',)

    class Meta:
        model = Addurlvet


admin.site.register(Addurlvet, AddurlvetAdmin)
