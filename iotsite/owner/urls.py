from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'owner'

router = routers.DefaultRouter()
router.register(r'position', views.PositionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
