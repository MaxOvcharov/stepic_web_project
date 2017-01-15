from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from qa.views import login_view, signup, quetion_add, popular, new

from qa import views

urlpatterns = patterns(
    url(r'^$', views.test),
    url(r'^login/$', views.test),
    url(r'^signup/$', views.test),
    url(r'^question/(\d+)$', views.test),
    url(r'^ask/.*$', views.test),
    url(r'^popular/$', views.test),
    url(r'^new/$', views.test),
)
)
