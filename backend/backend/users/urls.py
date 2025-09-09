from django.urls import path
from . import views

urlpatterns=[
    path('test--users-app/',views.test_view)
]