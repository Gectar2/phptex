from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Addurlteacher
# Register your models here.

class AddurlteacherAdmin(SummernoteModelAdmin):
    list_display = ['name_link', 'name_page']
    summernote_fields = ('content_text',)

    class Meta:
        model = Addurlteacher


admin.site.register(Addurlteacher, AddurlteacherAdmin)