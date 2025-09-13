
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import mark_attendance_view,PayrollViewSet,staffApi,staffDetailsView,shiftApi,ShiftDetailsView

router = DefaultRouter()
# router.register(r'staff', StaffViewSet, basename='staff')
# router.register(r'shift',ShifViewSet,basename="shift")
router.register(r'payroll',PayrollViewSet,basename="Payroll")

urlpatterns = [
    path('staff/',staffApi),
    path('staff/<int:id>/',staffDetailsView.as_view()),
    path('shift/',shiftApi),
    path('shift/<int:id>/',ShiftDetailsView.as_view()),
    path('attendance/mark/<int:shift_id>/',mark_attendance_view),
    path('', include(router.urls)),
]
