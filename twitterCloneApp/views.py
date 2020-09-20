from django.shortcuts import render, get_object_or_404, redirect
from twitterCloneApp.models import TwUser, TwTweet
from twitterCloneApp.forms import TwJoinForm, TwLoginForm
from django.db.models import Count, Avg
from django.contrib.auth import authenticate, login


# Create your views here.
def main(request):
    context = {}
    return render(request, 'main.html', context)


def join(request):
    if request.method == 'POST':
        join_form = TwJoinForm(request.POST)
        if join_form.is_valid():
            new_item = join_form.save()
            return redirect('main')
    # pass
    join_form = TwJoinForm()
    return render(request, 'join.html', {'form': join_form})


def user_login(request):
    if request.method == 'POST':
        login_form = TwLoginForm(request.POST)
        username = request.POST['user_id']
        password = request.POST['user_pwd']
        print(request.POST)
        user = authenticate(username=username, password=password)
        print("1", user)
        if user is not None:
        # if login_form.is_valid():
            login(request, user)
            print("2", user)
            return redirect('main')
    login_form = TwLoginForm()
    return render(request, 'login.html', {'form': login_form})