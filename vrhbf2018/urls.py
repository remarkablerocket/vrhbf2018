from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

import registration

from beerfest.views import user_profile
import beerfest


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("registration.backends.simple.urls")),
    path('accounts/profile/', user_profile, name='user_profile'),
    path('', include("beerfest.urls")),
]
