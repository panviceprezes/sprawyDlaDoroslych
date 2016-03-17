from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url('main', views.main, name='main'),
	url(r'^singleMovie/(\d{1})/$', views.singleMovie, name='singleMovie'),
	url(r'^saveSingleMovie/(\d{1})/$', views.saveSingleMovie, name='saveSingleMovie')
]