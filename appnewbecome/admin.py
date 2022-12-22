from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Addimgnews, Addnews
# Register your models here.


class Addimgnewstabularinline(admin.TabularInline):
    model = Addimgnews

class AddnewsAdmin(SummernoteModelAdmin):
    list_display = ['title', 'date_time']
    inlines = [Addimgnewstabularinline]
    summernote_fields = ('text_news',)

    class Meta:
        model = Addnews



admin.site.register(Addnews, AddnewsAdmin)

# @admin.register(Addnews)
# class AnsweroptionsblockPanel(admin.ModelAdmin):
#     pass