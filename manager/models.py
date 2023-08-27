from django.db import models

class Manager (models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Manager'

    def __str__(self) -> str:
        return self.name
