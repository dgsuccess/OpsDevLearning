from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weibo.views.home', name='home'),
    # url(r'^weibo/', include('weibo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', 'status.views.hello'),
    url(r'^index/', 'status.views.index'),
    url(r'^login/', 'status.views.login_view'),
    url(r'^logout/', 'status.views.logout_view'),
    url(r'^say/', 'status.views.say'),
)
