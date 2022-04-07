from django.urls import include
from django.urls import path
from rest_framework import routers
from . import views

# define the router
router = routers.DefaultRouter()

# define the URL prefix to use for this set of routes and the viewset class.
router.register(r'position', views.PositionViewSet)

# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
