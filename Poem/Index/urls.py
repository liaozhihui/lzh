# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns=[url(r"^main/$",views.main_views),
             url(r"^show/$",views.show_views),]