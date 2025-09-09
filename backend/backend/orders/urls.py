from django.urls import path
from . import views

urlpatterns=[
    path('test-orders-app/',views.test_view)
]