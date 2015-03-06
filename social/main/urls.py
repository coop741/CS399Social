from django.conf.urls import patterns, include, url
from django.contrib import admin
from views.home import home
from views.mood import mood
from views.feed_user import feed_user
from views.feed import feed


urlpatterns = patterns('',
                       # Examples:
                       url(r'^mood$', mood, name='mood'),
                       url(r'^mood/(?P<pk>\d+)', mood, name='mood_pk'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login$', 'django.contrib.auth.views.login'),
                       url(r'^logout$', 'django.contrib.auth.views.logout'),
                       url(r'^user/(?P<user_name>[-\w]+)/mood$', feed_user),
                       url(r'^feed$', feed),
                       url(r'^$', home)
                       )
