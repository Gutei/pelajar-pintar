from django.contrib import admin
from panel.models import StudentRegistration

@admin.register(StudentRegistration, site=admin.site)
class StudentRegistrationAdmin(admin.ModelAdmin):
    list_display = ('nisn', 'student_name', 'from_school', 'to_school')