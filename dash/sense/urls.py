from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from sense import views

app_name = 'School Sense'

admin.autodiscover()


class CustomAdminSite(admin.AdminSite):

    def get_urls(self):
        urls = []
        return urls


urlpatterns = [
                  url(r'^select2/', include('django_select2.urls')),
                  url(r'^$', views.school_sense, name='school_sense'),

                  url(r'^sense-sm-view/$', views.MajorList.as_view(), name='sm_view'),
                  url(r'^sense-sm-add/$', views.MajorCreate.as_view(), name='sm_add'),
                  url(r'^sense-sm-edit/(?P<pk>[^/]+)/$', views.MajorUpdate.as_view(), name='sm_edit'),
                  url(r'^sense-sm-delete/(?P<pk>[^/]+)/$', views.MajorDelete.as_view(), name='sm_delete'),

                  url(r'^sense-se-view/$', views.ExtracurricularList.as_view(), name='sex_view'),
                  url(r'^sense-se-add/$', views.ExtracurricularCreate.as_view(), name='sex_add'),
                  # url(r'^sense-se-edit/(?P<pk>[^/]+)/$', views.MajorUpdate.as_view(), name='sm_edit'),
                  url(r'^sense-se-delete/(?P<pk>[^/]+)/$', views.MajorDelete.as_view(), name='sex_delete'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
