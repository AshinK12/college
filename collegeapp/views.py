from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect



def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'E-mail Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,last_name=last_name,email=email)
                user.save()
                print('User created')
                return redirect('login')
        else:
            messages.info(request, 'Password mismatched')
            return redirect('register')
    else:

        return render(request, 'register.html')



def department_wikipedia(request, department):

    return redirect('https://en.wikipedia.org/wiki/' + department)
def course_wikipedia(request,course):
    return redirect('https://en.wikipedia.org/wiki/' + course)

def dashboard(request):
    return render(request, 'dashboard.html')

def form_view(request):

    return render(request, 'form.html')
