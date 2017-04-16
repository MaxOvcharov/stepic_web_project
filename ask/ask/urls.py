from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'qa.views.new_qa'),
                       url(r'^popular/.*$', 'qa.views.popular_qa'),
                       url(r'^question/(?P<qa_id>\d+)$', 'qa.views.question'),
                       url(r'^login/.*$', 'qa.views.test'),
                       url(r'^signup/.*$', 'qa.views.test'),
                       url(r'^ask/.*$', 'qa.views.test'),
                       url(r'^new/.*$', 'qa.views.test'),)
