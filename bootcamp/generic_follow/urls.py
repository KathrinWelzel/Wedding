from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(
        r'^follow/(?P<app>[^\/]+)/(?P<model>[^\/]+)/(?P<object_id>\d+)/$',
        'followit.views.follow_object',
        name = 'follow_object'
    ),
    url(
        r'^unfollow/(?P<app>[^\/]+)/(?P<model>[^\/]+)/(?P<object_id>\d+)/$',
        'followit.views.unfollow_object',
        name = 'unfollow_object'
    ),
    url(
        r'^toggle-follow/(?P<app>[^\/]+)/(?P<model>[^\/]+)/(?P<object_id>\d+)/$',
        'followit.views.toggle_follow_object',
        name='toggle_follow_object'
    )
)
