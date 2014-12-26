from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^blog/', include('facts.urls')),

    url(r'^admin/', include(admin.site.urls), name="admin"),
)
