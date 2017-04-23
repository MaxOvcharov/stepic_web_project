from django.conf.urls import include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = [
                       # Examples:
                       # url(r'^$', 'ask.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('qa.urls')),

                       #    url(r'^question/', include('qa.urls'), name='question'),
                       #    url(r'^$', 'views.test', name='home'),
                       #    url(r'^login/', 'views.test', name='login'),
                       #    url(r'^signup/', 'views.test', name='signup'),
                       #    url(r'^ask/', 'views.test', name='ask'),
                       #    url(r'^popular/', 'views.test', name='popular'),
                       #    url(r'^new/', 'views.test', name='new'),

               ]



