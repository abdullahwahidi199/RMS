
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StaffViewSet,ShifViewSet

router = DefaultRouter()
router.register(r'staff', StaffViewSet, basename='staff')
router.register(r'shift',ShifViewSet,basename="shift")

urlpatterns = [
    path('', include(router.urls)),
]
