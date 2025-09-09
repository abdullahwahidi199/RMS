from django.urls import path
from . import views

urlpatterns=[
    path('test-cus-app/',views.test_view)
]