from django.shortcuts import render, get_object_or_404, redirect
from twitterCloneApp.models import TwTweet, TwImages
from twitterCloneApp.forms import TwTweetForm
# ======================================================================================================


def get_list(request):
    id = request.session.get('id')

    # .get() 은 객체를 리턴한다
    tw_list = TwTweet.objects.all(user_id=id)

    # ref) 모델 간의 릴레이션을 이용하여 TwImages 에서 TwTweet Object 를 가져올 수 있다
    # tw_image_list = TwImages.objects.filter(tweet_id=30) # TwImages Object(2)
    # tweet = tw_image_list.tweet # TwTweet Object(30) (instance) (not iterable, onle one tweet)
    # user = tweet.user # user_nm = test

    print('===================================================')
    # print(tw_image_queryset.values())
    # tw_image_list = []
    # # <QuerySet [<TwTweet:TwTweet object(id=3)>, <>, <>, ...]> 의 형태
    # for tweet in tw_list:
    #     # queryset to list
    #     tw_image_queryset = TwImages.objects.filter(tweet=tweet.id).select_related('tweet').all()
    #     if len(tw_image_queryset) != 0:
    #         tw_image_list.append(tw_image_queryset)
    #         # print(tw_image_queryset.values())
    #     # tw_image_queryset = TwImages.objects.filter(tweet=tweet.id).select_related().values()

    return render(request, 'twc/home.html', {'list': tweet, 'image_list': tw_image_list})


def tweet(request):
    if request.method == 'GET':
        form = TwTweetForm()
        return render(request, 'twc/tweet.html', {'form': form})
    elif request.method == 'POST':
        form = TwTweetForm(request.POST)
        print('fileList:', request.FILES.getlist('images'))
        if form.is_valid():
            item = form.save(commit=True)
            for idx, image in enumerate(request.FILES.getlist('images')):
                print(idx, ':', image)
                image_form = TwImages()
                image_form.tweet = item   # TwImages.twTweet (FK) <== TwTweet.id (PK)
                image_form.image = image
                image_form.save()

            return redirect('twc:home')
    return


def update(request, id):
    item = get_object_or_404(TwTweet, pk=id)
    if request.method == 'GET':
        form = TwTweetForm(instance=item)

        return render(request, 'twc/update.html', {'form': form, 'id': item.id})
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
