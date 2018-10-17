from django.conf.urls import include
from django.urls import path

import beerfest.views

urlpatterns = [
    path('', beerfest.views.index, name='index'),
    path('beers/', beerfest.views.beer_list, name='beer_list'),
    path('beers/<int:id>', beerfest.views.beer_detail, name='beer_detail'),
]
