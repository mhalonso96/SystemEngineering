from rest_framework import viewsets
from ..models import TestLab
from .serializers import TestLabSerializer

class TestLabViewset (viewsets.ModelViewSet):
    queryset = TestLab.objects.all()
    serializer_class = TestLabSerializer