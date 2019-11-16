from django.contrib import admin
from panel.models import (School, SchoolContact, SchoolMajor, SchoolExtracurricular, SchoolAchievement,
                          SchoolActivity, AbstractSchool, SchoolMagazine, SchoolMagazineActivity, Province)

@admin.register(Province, site=admin.site)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('code', 'name',)
    search_fields = ('code', 'name',)