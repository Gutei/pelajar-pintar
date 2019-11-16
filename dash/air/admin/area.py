from django.contrib import admin
from panel.models import (School, SchoolContact, SchoolMajor, SchoolExtracurricular, SchoolAchievement,
                          SchoolActivity, AbstractSchool, SchoolMagazine, SchoolMagazineActivity, Province, City)

@admin.register(Province, site=admin.site)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('code', 'name',)
    search_fields = ('code', 'name',)

@admin.register(City, site=admin.site)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('province', 'code', 'name',)
    search_fields = ('province', 'code', 'name',)