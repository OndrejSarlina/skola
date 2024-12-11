from django.shortcuts import render, HttpResponse
from . models import * # importuje modely

# Create your views here.

def index(request):
    studenti = Student.objects.all()
    return HttpResponse(studenti)
