from django.contrib import admin
from .models import Department

@admin.register(Department)
class Department(admin.ModelAdmin):
    list_display =  ('name', 'leader')