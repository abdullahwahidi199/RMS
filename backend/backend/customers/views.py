from django.shortcuts import render
from django.http import HttpResponse

def test_view(requset):
    return HttpResponse("customers app is working fine")
# Create your views here.
