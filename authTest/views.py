from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from authTest.models import User
from authTest.mybackends import MyBackend
# from django.contrib.auth import authenticate, login
from authTest.forms import UserForm, LoginForm
from django.http import HttpResponse


# Create your views here.
def main(request):
    context = {}
    return render(request, 'test/main.html', context)


def join(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            return redirect('auth:main')
    else:
        form = UserForm()
        return render(request, 'test/join.html', {'form': form})


def user_login(request):
    mybackend = MyBackend()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user_id = request.POST['user_id']
        user_pwd = request.POST['user_pwd']
        user = mybackend.authenticate(request, user_id, user_pwd)
        print('1', user)
        if user is not None:
            mybackend.get_user(user_id)
            print('2', user)
            # login(request, user)
            return redirect('auth:main')
        else:
            return redirect('auth:login')
    else:
        form = LoginForm()
        return render(request, 'test/login.html', {'form': form})
