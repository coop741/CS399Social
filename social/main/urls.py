from django.conf.urls import patterns, include, url
from django.contrib import admin
from views.home import home

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home', name='home'),
    url(r'^mood$', 'main.views.mood', name='mood'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home)
)
