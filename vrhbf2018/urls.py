from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import beerfest.views

# Examples:
# url(r'^$', 'vrhbr2018.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', beerfest.views.index, name='index'),
    url(r'^db', beerfest.views.db, name='db'),
    path('admin/', admin.site.urls),
]
