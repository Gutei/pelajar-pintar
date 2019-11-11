from django.contrib import admin
from panel.models import School, SchoolContact, SchoolMajor, SchoolExtracurricular, SchoolAchievement, SchoolActivity


class SchoolContactInline(admin.TabularInline):
    model = SchoolContact
    extra = 1

class SchoolMajorInline(admin.TabularInline):
    model = SchoolMajor
    extra = 1

class SchoolExtracurricularInline(admin.TabularInline):
    model = SchoolExtracurricular
    extra = 1

@admin.register(School, site=admin.site)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'school_number')
    inlines = [
        SchoolContactInline,
        SchoolMajorInline,
    ]

@admin.register(SchoolExtracurricular, site=admin.site)
class SchoolExtracurricularAdmin(admin.ModelAdmin):
    list_display = ('school', 'name')


@admin.register(SchoolAchievement, site=admin.site)
class SchoolAchievementAdmin(admin.ModelAdmin):
    list_display = ('school', 'name')


@admin.register(SchoolActivity, site=admin.site)
class SchoolActivityAdmin(admin.ModelAdmin):
    list_display = ('school', 'title')