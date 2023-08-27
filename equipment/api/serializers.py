from rest_framework import serializers
from ..models import Equipment

class EquipmentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only= True)
    name = serializers.CharField(required= True)
    description  = serializers.CharField(required= True)
    vendor = serializers.CharField(required= True)
    email_vendor= serializers.EmailField(required= False)
    status = serializers.ChoiceField(choices=[('OK'), ('NOK')])
    note = serializers.CharField(required= False )
    has_license = serializers.BooleanField(required= True)
    version = serializers.CharField(required= False)
    ip_address = serializers.CharField(required= False)
    last_revision_at = serializers.DateField(required=True)
    last_revision_by = serializers.CurrentUserDefault()
    has_calibration = serializers.BooleanField(required= False)
    last_calibration_at = serializers.DateField(required=False)
    last_calibration_by = serializers.CharField(required=False)
        
    class Meta:
        model = Equipment
        fields = '__all__'

