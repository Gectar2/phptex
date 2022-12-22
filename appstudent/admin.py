from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Addurlstudent
# Register your models here.

class AddurlstudentAdmin(SummernoteModelAdmin):
    list_display = ['name_link', 'name_page']
    summernote_fields = ('content_text',)

    class Meta:
        model = Addurlstudent


admin.site.register(Addurlstudent, AddurlstudentAdmin)