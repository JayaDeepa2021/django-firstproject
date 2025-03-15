from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def house(request):
    return HttpResponse("this is first app")

def deepa(request):
    return HttpResponse("this is second app")