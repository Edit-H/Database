from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^main$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^travels$', views.travels),
	url(r'^travels/add$', views.add),
	url(r'^travels/added$', views.added),
	url(r'^logout$', views.logout),
	url(r'^home$', views.home),
	url(r'^joins/(?P<id>\d+)$', views.joins),
	url(r'^travels/destination/(?P<id>\d+)$', views.destination),

]