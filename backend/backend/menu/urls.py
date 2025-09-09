from django.urls import path
from . import views

urlpatterns=[
    path('test-menu-app/',views.test_view)
]