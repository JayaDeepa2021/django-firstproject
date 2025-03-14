from django.shortcuts import render
from django.http import HttpResponse


def house(request):
    return HttpResponse("Im in my house")


def deepa(request):
    return HttpResponse("Happy Birthday dear")