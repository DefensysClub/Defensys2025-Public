from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login
import os
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from finder.models import AcademicDivision, Department, Employee, Course

def index(request):
    return render(request, "index.html")

def search(request):
    results = AcademicDivision.objects.filter(**request.GET.dict())
    results = [result.name for result in results]
    
    return render(request, "results.html", {"results": results})

def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user is None:
            return HttpResponse("User not found.")
        
        elif user.password == password:
            login(request, user)
            return HttpResponse("User authenticated and logged in.")
        else:
            return HttpResponse("Failed to authenticate user.")
    return render(request, 'authenticate_user.html')


@user_passes_test(lambda u: u.is_authenticated and u.username == 'school_admin')
def flag(request):
    try:
        flag = os.getenv('FLAG', 'defensys{flag_not_set}')
    except:
        flag = "Flag not found. Please contact the admin."

    return HttpResponse("Hello, Admin. This page is only for you. And here is your flag: " + flag)

