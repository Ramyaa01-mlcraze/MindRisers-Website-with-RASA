from django.http import HttpResponse
from django.shortcuts import render
#from .models import TeacherDetails, User


# Create your views here.
def baseHome(request):
    return render(request,'baseHome.html')
def aboutus(request):
    return render(request,'aboutus.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def register_teacher(request):
    return render(request,'register-teacher.html')
def register_student(request):
    return render(request,'register-student.html')