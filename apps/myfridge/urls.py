from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='myfridge'),
    url(r'^/new$', views.new, name='newingr'),
    url(r'^/create$', views.create, name='makeingr'),
    url(r'^/add$', views.add, name='addingr'),
    url(r'^/ingrdb$', views.ingrdb, name='ingrdb'),
    url(r'^/(?P<ingr_id>\d+)$', views.read, name='viewingr'),
    url(r'^/(?P<ingr_id>\d+)/edit$', views.edit, name='editingr'),
    url(r'^/(?P<ingr_id>\d+)/update$', views.update, name='updateingr'),
    url(r'^/(?P<ingr_id>\d+)/destroy$', views.destroy, name='destroyingr'),
    url(r'^/(?P<ingr_name>\w+)/ingr_json$', views.ingrjson, name='ingrjson'),
]
