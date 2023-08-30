from rest_framework import serializers
from ..models import TestLab

class TestLabSerializer (serializers.ModelSerializer):
    class Meta:
        model = TestLab
        fields = '__all__'
        depth = 2