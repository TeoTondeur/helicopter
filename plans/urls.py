from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^intervalles$', views.intervalles, name='intervalles'),
    url(r'^radios$', views.radios, name='radios'),
]
