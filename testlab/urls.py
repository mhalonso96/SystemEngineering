from django.urls import include, path
from rest_framework import routers

from .api.viewsets import TestLabViewset


app_name = 'testlab'
router = routers.DefaultRouter()
router.register(r'testlab', TestLabViewset)
urlpatterns = [
    path("api/v1/", include(router.urls))
]