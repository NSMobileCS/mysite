from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/?$', views.index, name='index'),
    url(r'^(?P<pres_id>[0-9]+)/detail/?$', views.detail, name='detail'),
    url(r'^(?P<pres_id>[0-9]+)/?$', views.detail, name='detail'),
    url(r'^(?P<pres_id>[0-9]+)/voting/?$', views.voting, name='voting'),
    url(r'^(?P<pres_id>[0-9]+)/vote/?$', views.vote, name='votear'),
    url(r'^(?P<pres_id>[0-9]+)/voting/vote/?$', views.vote, name='vote'),
    url(r'^results/?$', views.all_results, name='allresults'),
    url(r'^results/(?P<pres_id>[0-9]+)/?$', views.results, name='results'),
]