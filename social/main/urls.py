from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home', name='home'),
    url(r'^mood$', 'main.views.mood', name='mood'),
    url(r'^admin/', include(admin.site.urls)),
)
