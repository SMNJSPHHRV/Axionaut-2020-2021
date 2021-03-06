"""axionaut_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from axionaut_app import views

urlpatterns = [
    url(r'^$', views.menu, name="menu"),
    url(r'^training/$', views.commandes, name="commandes"),
    url(r'^auto/$', views.auto, name='auto'),
    url(r'^admin/', admin.site.urls),
    url(r'^axionaut_app/', include(('axionaut_app.urls',
                                    'axionaut_app'), namespace='axionaut_app')),
    url(r'^start_stop/$', views.start_stop, name='start_stop'),
    url(r'^start_stop_auto/$', views.start_stop_auto, name='start_stop_auto'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
