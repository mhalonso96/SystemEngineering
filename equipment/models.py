from django.db import models
from django.contrib.auth.models import User

class Equipment(models.Model):
    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipments'
    name= models.CharField(max_length= 255)
    description = models.CharField(max_length= 1000)
    vendor = models.CharField(max_length= 255)
    email_vendor= models.CharField(max_length= 255)
    status = models.CharField(max_length=3,
                              choices=[('OK','OK'),('NOK','NOK'),],)
    note= models.CharField(max_length=2000)
    has_license = models.BooleanField(default= False)
    version = models.CharField(max_length=30, blank=True, null=True)
    ip_address = models.CharField(max_length=20, blank=True, null=True)
    last_revision_at = models.DateField(blank=True, null=True)
    last_revision_by  = models.ForeignKey(User, on_delete=models.CASCADE)
    has_calibration = models.BooleanField()
    last_calibration_at = models.DateField(blank=True, null=True)
    last_calibration_by = models.CharField(User,blank=True, null=True, max_length=255)
    cabinet = models.PositiveIntegerField()
    shelf = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name
