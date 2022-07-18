from ast import Not, Return
from email import message
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def index(request):
    if request.method == 'POST':
        username = request.POST['usname']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/welcome')
        else:
            messages.warning(request, "Invalid Credentials")
            return redirect('/')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('uname');
        email = request.POST.get('email');
        fname = request.POST.get('fname');
        lname = request.POST.get('lname');
        passw = request.POST.get('pass');

        if User.objects.filter(email = email).exists():
            messages.warning(request, "Email already exists")
            return redirect('/signup')

        if User.objects.filter(username = username).exists():
            messages.warning(request, "Username already exists")
            return redirect('/signup')

        user = User(username=username, email=email, first_name=fname, last_name=lname)
        user.set_password(passw)
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('/')
    return render(request, 'signup.html')

def welcome(request):
    return render(request, 'welcome.html')

def logoutUser(request):
    logout(request)
    messages.success(request, "Logged out")
    return redirect('/')
