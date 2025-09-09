
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def test_view(requset):
    return HttpResponse("orders app is working fine")