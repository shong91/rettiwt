from django.shortcuts import render, get_object_or_404, redirect
from twitterCloneApp.models import TwTweet, TwImages
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

        print('=====================================')
        print('fileList:', request.FILES.getlist('images'))
        if form.is_valid():
            item = form.save(commit=True)
            for idx, image in enumerate(request.FILES.getlist('images')):
                print(idx, ':', image)
                image_form = TwImages()
                image_form.twTweet = item
                image_form.image = image
                image_form.save()

            return redirect('twc:home')
    return


def update(request, id):
    item = get_object_or_404(TwTweet, pk=id)
    print(request.FILES)
    if request.method == 'GET':
        form = TwTweetForm(instance=item)

        return render(request, 'twc/update.html', {'fo'
                                                   'rm': form, 'id': item.id})
    elif request.method == 'POST':
        form = TwTweetForm(request.POST, request.FILES, instance=item)
        print(form)
        if form.is_valid():
            for img in request.FILES.getlist('image'):
                # Photo model(relation: TwTweet) 생성하여 photo.save()
                print('in for loop')
                print(img)
                # item.tw_image_url = img
                item = form.save(commit=True)
                pass
            # item.tw_image_url = request.POST['tw_image_url']
            # item.save()
            # item = form.save(commit=True)
        return redirect('twc:home')


def delete(request, id):
    item = get_object_or_404(TwTweet, pk=id)
    item.delete()
    return redirect('twc:home')
