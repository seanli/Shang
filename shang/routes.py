from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('shang.views',
    url(r'^$', 'index'),
    url(r'^logout/$', 'logout'),
    url(r'^api/user/add/$', 'api_user_add'),
    url(r'^api/user/login/$', 'api_user_login'),
    url(r'^api/post/list/$', 'api_post_list')
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls))
)
