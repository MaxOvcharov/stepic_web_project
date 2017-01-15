from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from qa.views import login_view, signup, quetion_add, popular, new

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ask.views.home, name='home'),
    url(r'^login/', login_view, name='login_view'),
    url(r'^signup/', signup, name='signup'),
    url(r'^ask/', quetion_add, name='ask'),
    url(r'^popular/', popular, name='popular'),
    url(r'^new/', new, name='new'),
    url(r'^question/(?P<id>\d+/$', quetion_add, name='answer_add'),
)
