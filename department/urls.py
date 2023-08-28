from django.urls import include, path
from rest_framework import routers

from .api.viewsets import DepartmentViewset


app_name = 'department'
router = routers.DefaultRouter()
router.register(r'department', DepartmentViewset)
urlpatterns = [
    path("api/v1/", include(router.urls))
]