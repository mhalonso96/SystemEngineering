from rest_framework import viewsets
from .serializers import DepartmentSerializer
from ..models import Department

class DepartmentViewset (viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer