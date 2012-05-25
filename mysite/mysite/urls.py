from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from polls.views import Home, Detail

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^poll/(?P<pk>\d+)/$', Detail.as_view(), name='polls-detail'),
    url(r'^admin/', include(admin.site.urls)),
)
