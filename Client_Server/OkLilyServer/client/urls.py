__author__ = 'Marc'
from django.conf.urls import patterns, url
from client import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'OkLilyServer.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^job/receiver', views.job_receiver),

                       )