from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from app.forms import *
# Create your views here.
def home(request):
    return render(request,'home.html')

def insert_school(request):
    ESFO=SchoolForms()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=SchoolForms(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data Inserted Successfully')
    return render(request,'insert_school.html',d)

def insert_student(request):
    ESFO=StudentForms()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=StudentForms(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data Inserted Successfully')
    return render(request,'insert_student.html',d)

def slist(request):
    allschools = School.objects.all()
    d = {'schools': allschools}
    return render(request, 'slist.html', d)

def display(request, pk):
    SO = School.objects.get(pk=pk)
    d = {'SO': SO}
    return render(request, 'display.html', d)