# users/serializers.py
from rest_framework import serializers
from .models import Staff,Shift,Attendance,Payroll

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields="__all__"

class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payroll
        fields="__all__"

# class ShiftMiniserializer(serializers.ModelSerializer):
#     class Meta:
#         model=Shift
#         fields='__all__'

class StaffSerializer(serializers.ModelSerializer):
    attendances=AttendanceSerializer(many=True,read_only=True)
    payrolls=PayrollSerializer(many=True,read_only=True)

    class Meta:
        model = Staff
        fields = "__all__"

class ShiftSerializer(serializers.ModelSerializer):
    staff=StaffSerializer(many=True,read_only=True)
    class Meta:
        model=Shift
        fields="__all__"

