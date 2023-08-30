from django.db import models
from technician.models import Technician
from equipment.models import Equipment

class Department (models.Model):
    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Department'
    name = models.CharField(max_length= 100)
    leader = models.ForeignKey(Technician, on_delete=models.CASCADE)
    equipment = models.ManyToManyField(Equipment)
    
    def __str__(self) -> str:
        return self.name
    