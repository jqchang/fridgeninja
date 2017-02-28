from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^process$', views.process),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout, name='logout'),
]
