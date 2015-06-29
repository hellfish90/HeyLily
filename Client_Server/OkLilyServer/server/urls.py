__author__ = 'Marc'
from django.conf.urls import patterns, url
from server import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'OkLilyServer.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^module/$', views.ListModule.as_view()),
                       url(r'^module/create$', views.ModuleCreate.as_view()),
                       url(r'^module/(?P<pk>\d+)/modify', views.ModuleModify.as_view(), name='module_modify'),

                       url(r'^plugin/$', views.PluginList.as_view()),
                       url(r'^plugin/create$', views.PluginCreate.as_view()),
                       url(r'^plugin/(?P<pk>\d+)/modify', views.PluginModify.as_view(), name='plugin_modify'),

                       url(r'^instruction/$', views.InstructionList.as_view()),
                       url(r'^instruction/create$', views.InstructionCreate.as_view()),
                       url(r'^instruction/(?P<pk>\d+)/modify', views.InstructionModify.as_view(), name="instruction_modify"),

                       url(r'^job/receiver', views.job_receiver),
                       )