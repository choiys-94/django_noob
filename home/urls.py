from django.conf.urls import patterns, include, url
from home.views import index, ViewBoard

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index, name = 'index'),
    url(r'^board/$', ViewBoard, name = 'viewboard'),
)
