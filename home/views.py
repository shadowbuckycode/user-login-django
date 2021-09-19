from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login


# password: arpit@admin123
# Create your views here.
def index(request):
    print(request.user.is_anonymous)
    if request.user.is_anonymous:
        return redirect('login')
    return render(request, 'index.html') 

def login_user(request):
    if request.method == 'POST':
        # check if user is authenticated
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password) 
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            print('yESSS')
            login(request, user)
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/login')
