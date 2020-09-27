from django.shortcuts import render, get_object_or_404, redirect
# 로그인 인증 관련
from twitterCloneApp.authmodel import TwUser
from twitterCloneApp.mybackends import MyBackend
# 이메일 인증 관련
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from twitterCloneApp.token import account_active_token
from twitterCloneApp.forms import TwJoinForm, TwLoginForm
from django.db.models import Count, Avg
from twitterCloneApp.models import TwTweet

mybackend = MyBackend()


# Create your views here.
def main(request):
    print(request.session.get('user_id'))
    context = {}
    return render(request, 'twc/main.html', context)


def join(request):
    if request.method == 'GET':
        join_form = TwJoinForm()
        return render(request, 'twc/join.html', {'form': join_form})
    elif request.method == 'POST':
        join_form = TwJoinForm(request.POST)
        if join_form.is_valid():
            user = TwUser.objects.create_user(**join_form.cleaned_data)
            user.is_active = False # 이메일 인증 전 유저 비활성화
            user.save()

            current_site = get_current_site(request)
            message = render_to_string('twc/activation_email.html', {
                'user': user,
                'domain': current_site.domain, # 127.0.0.1:8000
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_active_token.make_token(user) # 토큰값 생성
            })

            mail_title = '회원가입 인증 메일'
            mail_to = request.POST['user_email']
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.send()

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
        if user is not None and user.is_active:     # 로그인 인증 & 이메일 인증 완료 -> 로그인 성공
            mybackend.get_user(user_id)
            request.session['user_id'] = user_id
            return redirect('twc:home')
        else:                                        # 로그인 실패
            return redirect('twc:login')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = TwUser.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError): # TwUser.DoesNotExist
        user = None

    if user is not None and account_active_token.check_token(user, token):       # 토큰값 일치 여부 확인
        user.is_active = True
        user.save()
        mybackend.get_user(user.user_id)
        request.session['user_id'] = user.user_id
        return redirect('twc:home')

    else:
        return render(request, 'twc/main.html', {'error': '계정 활성화 오류'})
    return


def get_list(request):
    list = {}
    return render(request, 'twc/home.html', list)


def tweet(request):
    return