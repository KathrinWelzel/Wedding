from django.conf.urls import patterns, include, url

urlpatterns = patterns('bootcamp.generic_follow.views',
        url(r'^user/$', 'follow_user', name='follow_user'),
)
