from django.urls import include
from django.urls import path

from . import views


# specify URL Path for rest_framework
urlpatterns = [
    path('', views.index),
    path('login', views.login_view),
]


