from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


def login(request):
    if request.method == 'POST':
        user_name = request.POST['Username']
        password = request.POST['password']
        user = auth.authenticate(username=user_name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        user_name = request.POST['Username']
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        email = request.POST['e-mail']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name,
                                                email=email, password=password)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')

    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
