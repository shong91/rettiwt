from django.shortcuts import render, get_object_or_404, redirect
from twitterCloneApp.models import TwUser, TwTweet, UserBackend
from twitterCloneApp.forms import TwJoinForm, TwLoginForm
from django.db.models import Count, Avg
from django.contrib.auth import login


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
            print(join_form)
            new_user = TwUser.objects.create_user(**join_form.cleaned_data)
            print('pwd 1: ', new_user.user_pwd)

            new_user.save()
            print('pwd 2: ', new_user.user_pwd)
            return redirect('main')


def user_login(request):
    if request.method == 'GET':
        login_form = TwLoginForm()
        return render(request, 'twc/login.html', {'form': login_form})
    elif request.method == 'POST':
        login_form = TwLoginForm(request.POST)
        user_id = request.POST['user_id']
        user_pwd = request.POST['user_pwd']
        user = TwUser.objects.get(user_id=user_id)
        print(1, user)
        if user is not None:
            # login(request, user)
            print(2, user)
            return redirect('main')
        return redirect('login')

        # userbackend = UserBackend()
        # user = userbackend.authenticate(user_id=user_id, user_pwd=user_pwd)
