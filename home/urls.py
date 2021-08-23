from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('' ,home ,name="home"),
    path('payment/', views.payment ,name="payment"),
]