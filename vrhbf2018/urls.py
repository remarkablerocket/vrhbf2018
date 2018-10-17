from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path('accounts/', include("registration.backends.simple.urls")),
    path('', include("beerfest.urls")),
]
