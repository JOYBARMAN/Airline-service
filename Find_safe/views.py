from django.shortcuts import render
from django.http import HttpResponse


def safe(request):
    return render(request,'findsafe.html')
