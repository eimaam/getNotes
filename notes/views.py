import email
from re import L
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
import os

from .models import Upload

# Create your views here.

def signup(request):
    if request.method == "POST":
        username = request.POST['userName']
        email = request.POST['emailEntry']
        password = request.POST['passwordEntry']
        password2 = request.POST['passwordEntry2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Is Already Registered')
                    return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('LandingPage')
        else:
            messages.info(request, 'Password And Confirm Password Must Be The Same')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['userName']
        password = request.POST['passwordEntry']

        if User.objects.filter(username=username).exists():
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Password Is Incorrect')
                return redirect('LandingPage')
        else:
            messages.info(request, 'User Does Not Exist')
            return redirect('LandingPage')
    else:
        return render(request, 'login.html')


def dashboard(request):
    elect_files = Upload.objects.filter(category="Electrical & Electronics Engineering")
    computer_files = Upload.objects.filter(category="Computer Engineering")
    other_files = Upload.objects.filter(category="Others")
    context = {
        'elect_files': elect_files,
        'computer_files': computer_files,
        'other_files': other_files,
        'MEDIA_URL' : settings.MEDIA_URL
    }
    return render(request, 'index.html', context)


def upload(request):
    if request.method == "POST":
        categoryEntry = request.POST['category']
        course_code = request.POST['courseCode']
        course_title = request.POST['courseTitle']
        pdf1 = Upload()
        pdf1.category = categoryEntry
        pdf1.courseCode = course_code
        pdf1.courseTitle = course_title
        pdf1.file = request.FILES['file']
        pdf1.user = request.user
        pdf1.save()
        return redirect('upload')
    return render(request, 'upload.html')

def logout(request):
    auth.logout(request)
    return redirect('LandingPage')