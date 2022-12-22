from django.contrib import admin
from .models import Blockinfoaboutcollege, Infodirector, Virtualtour, Ourprojects, Usefullinks, Ourpartners, Fillemodels, SiteDopmodels, Currentinfo
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Blockinfoaboutcollege)
class BlockinfoaboutcollegeAdmin(admin.ModelAdmin):
    list_display = ['title_college']

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Infodirector)
class InfodirectorAdmin(admin.ModelAdmin):
    list_display = ['title']

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Virtualtour)
class VirtualtourAdmin(admin.ModelAdmin):
    list_display = ['link_video']

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Ourprojects)
class OurprojectsAdmin(admin.ModelAdmin):
    list_display = ['link_project']

@admin.register(Usefullinks)
class OurprojectsAdmin(admin.ModelAdmin):
    list_display = ['link_useful']

@admin.register(Ourpartners)
class OurprojectsAdmin(admin.ModelAdmin):
    list_display = ['link_partners']
@admin.register(Currentinfo)
class CurrentinfoAdmin(admin.ModelAdmin):
    list_display = ['link_curinfo']

@admin.register(Fillemodels)
class OurprojectsAdmin(admin.ModelAdmin):
    list_display = ['title_name']



class SitedpmodelsAdmin(SummernoteModelAdmin):
    list_display = ['name_page', 'name_link']
    summernote_fields = ('content_text',)

    class Meta:
        model = SiteDopmodels


admin.site.register(SiteDopmodels, SitedpmodelsAdmin)


admin.site.site_title = "Администрирование сайта ФИЗтех"
admin.site.site_header = "Администрирование сайта ФИЗтех"