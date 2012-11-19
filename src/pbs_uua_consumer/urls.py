from django.conf.urls.defaults import *
"""
The consumer defines several views that need to be mapped
for communication with an OpenId endpoint.

login - openid request creation method. begins an openid flow
complete - handles an openid response
logo.gif - serves the openid logo for frontend
"""
urlpatterns = patterns('pbs_uua_consumer.views',
	url(r'^login/admin/(?P<popup_mode>0|1)/$', 'login_begin', {'to_admin': 1}, 'login_begin_admin_popup'),
	url(r'^login/admin/$', 'login_begin', {'to_admin': 1}, 'login_begin_admin'),
    url(r'^login/(?P<popup_mode>0|1)/$', 'login_begin', name='login_begin_popup'),
    url(r'^login/$', 'login_begin', name='login_begin'),
    url(r'^logo.gif$', 'logo', name='openid-logo'),
	url(r'^complete/(?P<admin>0|1)/$', 'login_complete', name='login_complete_admin'),
    (r'^complete/$', 'login_complete'),
)
