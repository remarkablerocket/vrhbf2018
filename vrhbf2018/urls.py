from django.conf.urls import include, url
from django.urls import path

from beerfest.views import user_profile


urlpatterns = [
    path('accounts/', include("registration.backends.simple.urls")),
    path('accounts/profile/', user_profile, name='user_profile'),
    path('', include("beerfest.urls")),
]
