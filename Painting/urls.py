"""Painting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url, include
from django.views.static import serve
from django.conf import settings

from mainapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('mainapp.urls', namespace='mainapp')),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'register/$', views.register),  # 注册
    url(r'login/$', views.login),  # 登录
    url(r'collect/$', views.collection),  # 收藏
    url(r'friend/$', views.friend),  # 朋友圈


    url(r'hqz/$',views.hqz),
]
