from django.contrib import admin
from panel.models import StudentRegistrationToken, SchoolToken
from rest_framework.authtoken.models import Token

@admin.register(StudentRegistrationToken, site=admin.site)
class StudentRegistrationTokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'token', 'expired_date', 'is_expired', 'created')

@admin.register(SchoolToken, site=admin.site)
class SchoolTokenTokenAdmin(admin.ModelAdmin):
    list_display = ('school', 'token', 'expired_date', 'is_expired', 'created')
