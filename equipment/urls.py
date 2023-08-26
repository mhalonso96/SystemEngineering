from django.urls import include, path
from rest_framework import routers

from .api.viewsets import EquipmentViewSet
app_name = 'equipment'
router = routers.DefaultRouter()
router.register(r'equipments', EquipmentViewSet)
urlpatterns = [
    path("api/v1/", include(router.urls))
]