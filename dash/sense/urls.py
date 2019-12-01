from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, LogoutView
from sense import views

app_name = 'School Sense'

admin.autodiscover()


class CustomAdminSite(admin.AdminSite):

    def get_urls(self):
        urls = []
        return urls


urlpatterns = [
                  url(r'^select2/', include('django_select2.urls')),
                  url(r'^admin/', admin.site.urls),
                  url(r'^login/$', LoginView.as_view(template_name='sense/login/login.html'), name="login"),
                  url(r'^$', views.school_sense, name='school_sense'),

                  # url(r'^logout/$', LogoutView.as_view(template_name='gdashboard/logout.html'), name='logout'),

                  url(r'^sense-sm-view/$', views.MajorList.as_view(), name='sm_view'),
                  url(r'^sense-sm-add/$', views.MajorCreate.as_view(), name='sm_add'),
                  url(r'^sense-sm-edit/(?P<pk>[^/]+)/$', views.MajorUpdate.as_view(), name='sm_edit'),
                  url(r'^sense-sm-delete/(?P<pk>[^/]+)/$', views.MajorDelete.as_view(), name='sm_delete'),

                  url(r'^sense-se-view/$', views.ExtracurricularList.as_view(), name='sex_view'),
                  url(r'^sense-se-add/$', views.ExtracurricularCreate.as_view(), name='sex_add'),
                  url(r'^sense-se-edit/(?P<pk>[^/]+)/$', views.ExtracurricularUpdate.as_view(), name='sex_edit'),
                  url(r'^sense-se-delete/(?P<pk>[^/]+)/$', views.ExtracurricularDelete.as_view(), name='sex_delete'),

                  url(r'^sense-sac-view/$', views.ActivityList.as_view(), name='sac_view'),
                  url(r'^sense-sac-add/$', views.ActivityCreate.as_view(), name='sac_add'),
                  url(r'^sense-sac-edit/(?P<pk>[^/]+)/$', views.ActivityUpdate.as_view(), name='sac_edit'),
                  url(r'^sense-sac-delete/(?P<pk>[^/]+)/$', views.ActivityDelete.as_view(), name='sac_delete'),

                  url(r'^sense-sachiev-view/$', views.AchievementList.as_view(), name='sachiev_view'),
                  url(r'^sense-sachiev-add/$', views.AchievementCreate.as_view(), name='sachiev_add'),
                  url(r'^sense-sachiev-edit/(?P<pk>[^/]+)/$', views.AchievementUpdate.as_view(), name='sachiev_edit'),
                  url(r'^sense-sachiev-delete/(?P<pk>[^/]+)/$', views.AchievementDelete.as_view(), name='sachiev_delete'),

                  url(r'^sense-steach-view/$', views.TeacherList.as_view(), name='steach_view'),
                  url(r'^sense-steach-add/$', views.TheacherCreate.as_view(), name='steach_add'),
                  url(r'^sense-steach-edit/(?P<pk>[^/]+)/$', views.TeacherUpdate.as_view(), name='steach_edit'),
                  url(r'^sense-steach-delete/(?P<pk>[^/]+)/$', views.TeacherDelete.as_view(), name='steach_delete'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
