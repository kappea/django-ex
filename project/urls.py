from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

# from welcome.views import index, health
from welcome.views import health

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', index),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('mainscreen.urls')),
    url(r'^', include('evenementen.urls', namespace="evenementen")),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'mainscreen/login.html'}, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^accounts/password_reset/$', auth_views.password_reset, {'template_name': 'mainscreen/password_reset.html'}, name='password_reset'),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^survey/', include('survey.urls')),
]
