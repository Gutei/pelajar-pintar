from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from sense import views

app_name = 'sense register'

admin.autodiscover()


class CustomAdminSite(admin.AdminSite):

    def get_urls(self):
        urls = []
        return urls


urlpatterns = [
                  url(r'^select2/', include('django_select2.urls')),
                  url(r'', views.register, name='school-register'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
