
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StaffViewSet,ShifViewSet,mark_attendance_view,PayrollViewSet

router = DefaultRouter()
router.register(r'staff', StaffViewSet, basename='staff')
router.register(r'shift',ShifViewSet,basename="shift")
router.register(r'payroll',PayrollViewSet,basename="Payroll")

urlpatterns = [
    path('attendance/mark/<int:shift_id>/',mark_attendance_view),
    path('', include(router.urls)),
]
