from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from rest_framework import routers
from api.views import SchoolViewSet, TeacherViewSet, StudentRegistrationViewSet

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pelajar Pintar API',)

# Routers provide an easy way of automatically determining the URL conf.
school_router = routers.SimpleRouter(trailing_slash=False)
school_router.register(r'', SchoolViewSet)

teacher_router = routers.SimpleRouter(trailing_slash=False)
teacher_router.register(r'', TeacherViewSet)

student_registration_router = routers.SimpleRouter(trailing_slash=False)
student_registration_router.register(r'', StudentRegistrationViewSet)

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^schools/', include(school_router.urls)),
    url(r'^teachers/', include(teacher_router.urls)),
    url(r'^psb/', include(student_registration_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)