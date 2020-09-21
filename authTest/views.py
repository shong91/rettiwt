from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from authTest.forms import UserForm, LoginForm
from django.http import HttpResponse


# Create your views here.
def main(request):
    context = {}
    return render(request, 'test/main.html', context)


def join(request):
    if request.method == 'POST':
        print('hello 1')
        form = UserForm(request.POST)
        if form.is_valid():
            print('hello 2')
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('auth:main')
    else:
        form = UserForm()
        return render(request, 'test/join.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        print(form)
        print(form.is_valid())
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('auth:main')
        else:
            return redirect('auth:login')
    else:
        form = LoginForm()
        return render(request, 'test/login.html', {'form': form})
