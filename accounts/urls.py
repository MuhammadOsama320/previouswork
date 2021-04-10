from django.contrib import admin
from django.urls import path, include

from accounts import views

urlpatterns = [

    path('', views.index, name="credential"),
    path('login', views.login, name="login"),
    # path('logout', views.logout, name="credential"),
]
