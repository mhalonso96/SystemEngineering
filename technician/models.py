from django.db import models

class Technician(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Technician"
        verbose_name_plural = "Technician"

    def __str__(self) -> str:
        return self.name
