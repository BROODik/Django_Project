from django.http import HttpResponse
from django.shortcuts import render

def project(request):
    return render(request, 'project.html')