from django.contrib import admin
from django.urls import path, re_path, include

import stu
from . import views

urlpatterns = [
    re_path(r'^$', views.setcookie)
]