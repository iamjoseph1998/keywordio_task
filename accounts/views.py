from django.contrib.auth import models
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        #Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Password validation
        if password == password2:
            if User.objects.filter(email=email).exists():
                # messages.error(request, 'Email already exist')
                return redirect('register')
            else:
                first_name = first_name.capitalize()
                last_name = last_name.capitalize()
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                password=password)
                # messages.success(request, 'Registered successfully')
                return redirect('register')
        else:
            # messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        #Credentials match
        if user is not None:
            auth.login(request, user)
            
            return redirect('adminapp/home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('/')
    else:
        if request.user.is_authenticated:
            return redirect('adminapp/home')
        else:
            return render(request, 'login.html')

@login_required(login_url="/")
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # messages.success(request, 'Logged out successfully')
        return redirect('/')