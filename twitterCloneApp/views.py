from django.shortcuts import render, get_object_or_404, redirect
from twitterCloneApp.authmodel import TwUser
from twitterCloneApp.mybackends import MyBackend
from twitterCloneApp.models import TwTweet
from twitterCloneApp.forms import TwJoinForm, TwLoginForm
from django.db.models import Count, Avg

mybackend = MyBackend()


# Create your views here.
def main(request):
    context = {}
    return render(request, 'twc/main.html', context)


def join(request):
    if request.method == 'GET':
        join_form = TwJoinForm()
        return render(request, 'twc/join.html', {'form': join_form})
    elif request.method == 'POST':
        join_form = TwJoinForm(request.POST)
        if join_form.is_valid():
            new_user = TwUser.objects.create_user(**join_form.cleaned_data)
            print(new_user.user_pwd)
            return redirect('twc:main')


def user_login(request):
    if request.method == 'GET':
        login_form = TwLoginForm()
        return render(request, 'twc/login.html', {'form': login_form})
    elif request.method == 'POST':
        login_form = TwLoginForm(request.POST)
        user_id = request.POST['user_id']
        user_pwd = request.POST['user_pwd']
        user = mybackend.authenticate(request, user_id, user_pwd)
        if user is not None:     # 로그인 성공
            mybackend.get_user(user_id)
            return redirect('twc:main')
        else:    # 로그인 실패
            return redirect('twc:login')
