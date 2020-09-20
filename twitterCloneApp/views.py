from django.shortcuts import render, get_object_or_404, redirect
from twitterCloneApp.models import TwUser, TwTweet
from twitterCloneApp.forms import TwJoinForm, TwLoginForm
from django.db.models import Count, Avg


# Create your views here.
def main(request):
    context = {}
    return render(request, 'main.html', context)


def join_form(request):
    form = TwJoinForm()
    return render(request, '/joinForm.html', {'form': form})