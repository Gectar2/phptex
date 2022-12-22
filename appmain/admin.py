from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Addurlmain
# Register your models here.

class AddurlmainAdmin(SummernoteModelAdmin):
    list_display = ['name_link', 'name_page']
    summernote_fields = ('content_text',)

    class Meta:
        model = Addurlmain


admin.site.register(Addurlmain, AddurlmainAdmin)