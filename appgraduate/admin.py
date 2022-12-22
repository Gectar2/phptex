from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Addurlgraduate
# Register your models here.

class AddurlgraduateAdmin(SummernoteModelAdmin):
    list_display = ['name_link', 'name_page']
    summernote_fields = ('content_text',)

    class Meta:
        model = Addurlgraduate


admin.site.register(Addurlgraduate, AddurlgraduateAdmin)