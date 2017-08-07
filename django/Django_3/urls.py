"""Django_3 URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django_web.views import index
from django_web.views import chart
from django_web.views import chart_someone
from django_web.views import aboutus
from django_web.views import location
from django_web.views import other
from django_web.views import other_menu
from django_web.views import china
from django_web.views import chart1

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index),
    url(r'^chart/', chart),
    url(r'^chart_someone/', chart_someone),
    url(r'^aboutus/', aboutus),
    url(r'^location/', location),
    url(r'^other/', other),
    url(r'^other_menu/', other_menu),
    url(r'^china/', china),
    url(r'^chart_l/', chart1),

]
