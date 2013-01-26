from django.conf.urls import patterns, url

urlpatterns = patterns('', 
    url(r'^post/$', 'post_and_get_request_example.views.post_view', name='post_request_example'),
    url(r'^get/$', 'post_and_get_request_example.views.get_view', name='get_request_example'),
)