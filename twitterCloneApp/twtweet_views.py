from django.shortcuts import render, get_object_or_404, redirect
from twitterCloneApp.models import TwTweet
from twitterCloneApp.forms import TwTweetForm
# tweet CRUD ======================================================================================================


def list(request):
    id = request.session.get('id')
    # tlqkf 이게 어떻게 되는거야 어떻게 알고 TwTweet.user_id(number)로 조인해서 TwUser.user_id(string) 을 가져오는거임
    tw_list = TwTweet.objects.filter(user_id=id).select_related().all()

    return render(request, 'twc/home.html', {'list': tw_list})


def tweet(request):
    if request.method == 'GET':
        form = TwTweetForm()
        return render(request, 'twc/tweet.html', {'form': form})
    elif request.method == 'POST':
        form = TwTweetForm(request.POST)
        if form.is_valid():
            print(form)
            form.save(commit=True)
            return redirect('twc:home')
    return


def update(request, id):
    item = get_object_or_404(TwTweet, pk=id)
    if request.method == 'GET':
        form = TwTweetForm(instance=item)
        return render(request, 'twc/update.html', {'form': form, 'id': item.id})
    elif request.method == 'POST':
        form = TwTweetForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=True)
        return redirect('twc:home')


def delete(request, id):
    item = get_object_or_404(TwTweet, pk=id)
    item.delete()
    return redirect('twc:home')
