# users/views.py
from rest_framework import viewsets
from .models import Staff,Shift,Payroll
from .serializers import StaffSerializer,ShiftSerializer,PayrollSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class ShifViewSet(viewsets.ModelViewSet):
    queryset=Shift.objects.all()
    serializer_class=ShiftSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date
from .models import Staff, Shift, Attendance

@api_view(['POST'])
def mark_attendance_view(request):
    
    attendance_data = request.data.get('attendance', [])
    attendance_date = request.data.get('date', str(date.today()))

    if not attendance_data:
        return Response({'error': 'No attendance data provided.'}, status=status.HTTP_400_BAD_REQUEST)

    for record in attendance_data:
        staff_id = record.get('staff_id')
        shift_id = record.get('shift_id')
        status_value = record.get('status', 'Present')

      
        try:
            staff = Staff.objects.get(id=staff_id)
        except Staff.DoesNotExist:
            continue  

       
        shift = None
        if shift_id:
            try:
                shift = Shift.objects.get(id=shift_id)
            except Shift.DoesNotExist:
                shift = None

        
        Attendance.objects.update_or_create(
            staff=staff,
            shift=shift,
            date=attendance_date,
            defaults={'status': status_value}
        )

    return Response({'message': 'Attendance marked successfully!'}, status=status.HTTP_200_OK)


class PayrollViewSet(viewsets.ModelViewSet):
    queryset=Payroll.objects.all().order_by('-generated_at')
    serializer_class=PayrollSerializer