from django.conf.urls import url
from . import views

Purlpatterns = [
# default home page /music/
	url(r'^$', views.index, name='index'),
					
# default home page /music/id#
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

]
