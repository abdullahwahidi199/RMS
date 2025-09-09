# users/views.py
from rest_framework import viewsets
from .models import Staff,Shift
from .serializers import StaffSerializer,ShiftSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class ShifViewSet(viewsets.ModelViewSet):
    queryset=Shift.objects.all()
    serializer_class=ShiftSerializer