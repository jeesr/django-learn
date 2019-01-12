"""untitled1 URL Configuration

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
from django.urls import include,path

from app1 import views as app1_views     #从APP1导入views.py

urlpatterns = [
    path('', app1_views.index),#app1_views是上面定义的；index是views.py里面的函数
    path('admin/', admin.site.urls),
    path('add/<a>/<b>', app1_views.add, name='add'),
    path('getfun/<a>/<b>', app1_views.getfun, name='getfun'),
    path('create_article/', app1_views.create_article),
]
