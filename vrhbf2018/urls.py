from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

import registration

from beerfest.views import UserProfileView
import beerfest


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("registration.backends.simple.urls")),
    path('accounts/profile/', UserProfileView.as_view(), name='user-profile'),
    path('', include("beerfest.urls")),
]
