from django.conf.urls import patterns, include, url
from django.contrib import admin
from views.home import home
from views.mood import mood

urlpatterns = patterns('',
                       # Examples:
                       url(r'^mood$', mood, name='mood'),
                       url(r'^mood/(?P<pk>\d+)', mood, name='mood_pk'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', home)
                       )
