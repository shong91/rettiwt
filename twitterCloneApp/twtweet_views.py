from django.shortcuts import render, get_object_or_404, redirect
from twitterCloneApp.models import TwTweet, TwImages
from twitterCloneApp.forms import TwTweetForm
# ======================================================================================================


def get_list(request):
    id = request.session.get('id')
    print('/twc/home/ id: ', id)
    # .get() 은 객체를 리턴한다
    tw_list = TwTweet.objects.filter(user_id=id).order_by('-updated_at')
    for idx, tweet in enumerate(tw_list):
        user = tweet.user
        setattr(tweet, 'user_nm', user.user_nm)
        setattr(tweet, 'user_prof_pic', user.user_prof_pic)

    # ref) 모델 간의 릴레이션을 이용하여 TwImages 에서 TwTweet Object 를 가져올 수 있다
    # tw_image_list = TwImages.objects.filter(tweet_id=30) # TwImages Object(2)
    # tweet = tw_image_list.tweet # TwTweet Object(30) (instance) (not iterable, onle one tweet)
    # user = tweet.user # user_nm = test

    print('===================================================')
    return render(request, 'twc/home.html', {'list': tw_list})


def tweet(request):
    if request.method == 'GET':
        form = TwTweetForm()
        return render(request, 'twc/tweet.html', {'form': form})
    elif request.method == 'POST':
        form = TwTweetForm(request.POST)
        print('fileList:', request.FILES.getlist('image'))
        if form.is_valid():
            item = form.save(commit=True)
            item.save()
            for idx, image in enumerate(request.FILES.getlist('image')):
                print(idx, ':', image)
                item.image = image  # 이대로는 마지막 데이터만 들어감..
                item.save()

        return redirect('twc:home')
    # return


def update(request, id):
    item = get_object_or_404(TwTweet, pk=id)
    if request.method == 'GET':
        form = TwTweetForm(instance=item)
        image = item.image
        print(image)
        return render(request, 'twc/update.html', {'form': form, 'image': image, 'id': item.id})
    elif request.method == 'POST':
        form = TwTweetForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            for img in request.FILES.getlist('image'):
                # Photo model(relation: TwTweet) 생성하여 photo.save()
                # item.tw_image_url = img
                item = form.save(commit=True)
                item.image = img
                item.save()
            return redirect('twc:home')


def delete(request, id):
    item = get_object_or_404(TwTweet, pk=id)
    item.delete()
    return redirect('twc:home')
