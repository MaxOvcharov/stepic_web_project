from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qa.views',
                       url(r'^question/(?P<qa_id>\d+)/', 'question', name='question'),
                       url(r'^popular/', 'popular', name='popular'),
                       url(r'^ask/', 'ask', name='ask'),
                       url(r'^answer/', 'answer', name='answer'),
                       url(r'^login/', 'my_login', name='login'),
                       url(r'^signup/', 'signup', name='signup'),
                       url(r'^$', 'main', name='main'), )
