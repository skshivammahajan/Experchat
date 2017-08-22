"""ExperChat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from config.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^v1/', include('api.v1.urls', namespace='v1')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^api-auth/', include('rest_framework.urls',
                                           namespace='rest_framework')),
    ]


if settings.ENABLE_API_ROOT:
    urlpatterns += [
        url(r'^admin/', admin.site.urls),
        url(r'^api-auth/', include('rest_framework.urls',
                                           namespace='rest_framework')),
    ]