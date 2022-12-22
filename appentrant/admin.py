from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Addurlentrant
# Register your models here.

class AddurlentrantAdmin(SummernoteModelAdmin):
    list_display = ['name_link', 'name_page']
    summernote_fields = ('content_text',)

    class Meta:
        model = Addurlentrant


admin.site.register(Addurlentrant, AddurlentrantAdmin)