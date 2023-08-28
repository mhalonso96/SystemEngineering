from django.db import models
from manager.models import Manager
from technician.models import Technician
from department.models import Department

class TestLab(models.Model):
    class Meta:
        verbose_name = 'Test Lab'
        verbose_name_plural =  'Test Lab'
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE )
    technician = models.ManyToManyField(Technician)
    department = models.ManyToManyField(Department)
    

    def __str__(self) -> str:
        return f'Test Lab'
