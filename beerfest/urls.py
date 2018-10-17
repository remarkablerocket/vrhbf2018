from django.conf.urls import include, url
from django.urls import path

import beerfest.views

urlpatterns = [
    url(r'^$', beerfest.views.beer_list, name='index'),
]
