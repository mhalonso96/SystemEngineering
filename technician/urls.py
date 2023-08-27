from django.urls import include, path
from rest_framework import routers

from .api.viewsets import TechnicianViewSet


app_name = 'technician'
router = routers.DefaultRouter()
router.register(r'technician', TechnicianViewSet)
urlpatterns = [
    path("api/v1/", include(router.urls))
]