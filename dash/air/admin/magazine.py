from django.contrib import admin
from panel.models import (School, SchoolContact, SchoolMajor, SchoolExtracurricular, SchoolAchievement,
                          SchoolActivity, AbstractSchool, SchoolMagazine, SchoolMagazineActivity)

@admin.register(SchoolMagazine, site=admin.site)
class SchoolMagazineAdmin(admin.ModelAdmin):
    list_display = ('title', 'school', 'published_date',)


@admin.register(SchoolMagazineActivity, site=admin.site)
class SchoolMagazineActivityAdmin(admin.ModelAdmin):
    list_display = ('magazine', 'activity',)