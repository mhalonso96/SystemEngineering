from django.urls import include, path
from rest_framework import routers

from .api.viewsets import ManagerViewSet


app_name = 'manager'
router = routers.DefaultRouter()
router.register(r'manager', ManagerViewSet)
urlpatterns = [
    path("api/v1/", include(router.urls))
]