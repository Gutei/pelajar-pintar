from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from schoreg import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.contrib.auth.models import User

app_name = 'school register'

admin.autodiscover()


class CustomAdminSite(admin.AdminSite):

    def get_urls(self):
        urls = []
        return urls


urlpatterns = [
                  url(r'^jet/', include('jet.urls', 'jet')),
                  url(r'^ckeditor/', include('ckeditor_uploader.urls')),
                  url(r'^b4ck0ff1c3/', admin.site.urls),
                  url(r'', views.register, name='school-register'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
