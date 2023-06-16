from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'base.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = request.POST(authenticate(request, username=username, password=password))
        if user is not None:
            login(request, user)
            print('work')
            return redirect('login')


def SignupPage(request):
    if request.method == 'POST':
        print(request.POST)
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login_true.html')

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')