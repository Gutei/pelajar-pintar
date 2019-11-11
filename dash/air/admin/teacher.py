from django.contrib import admin
from panel.models import Teacher, TeacherContact

class TeacherContactInline(admin.TabularInline):
    model = TeacherContact
    extra = 1

@admin.register(Teacher, site=admin.site)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'school',)
    inlines = [
        TeacherContactInline,
    ]