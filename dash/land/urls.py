from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

from land import views

admin.site.site_header = 'Administraion Tools'

urlpatterns = [
                  url(r'^ckeditor/', include('ckeditor_uploader.urls')),
                  # url(r'^(?P<name>[^/]+)/(?P<pk>[^/]+)/', views.profile),
                  url(r'^$', views.profile, name='home'),
                  url(r'^About/$', views.contact, name='contact'),
                  url(r'^pengajar/$', views.teacher, name='teacher'),
                  url(r'^ekstrakurikuler/$', views.extracurriculer, name='extracurr'),
                  url(r'^kegiatan/$', views.activity, name='activity'),
                  url(r'^detail_kegiatan/(?P<id>[^/]+)/$', views.activity_view, name='activity_details'),
                  url(r'^prestasi/$', views.achiev, name='achiev'),
                  url(r'^detail_prestasi/(?P<id>[^/]+)/$', views.achiev_view, name='achiev_details'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
