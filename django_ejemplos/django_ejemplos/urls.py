from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^post-and-get-example/', include('post_and_get_request_example.urls')),

    # Examples:
    # url(r'^$', 'django_ejemplos.views.home', name='home'),
    # url(r'^django_ejemplos/', include('django_ejemplos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
