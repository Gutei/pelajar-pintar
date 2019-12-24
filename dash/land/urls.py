from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

from land import views

admin.site.site_header = 'Administraion Tools'

urlpatterns = [
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^(?P<name>[^/]+)/(?P<pk>[^/]+)/', views.profile),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)