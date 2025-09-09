# users/serializers.py
from rest_framework import serializers
from .models import Staff,Shift

class StaffSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Staff
        fields = "__all__"

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shift
        fields="__all__"