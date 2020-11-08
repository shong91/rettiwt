from django.urls import path
from . import twuser_views, twtweet_views
urlpatterns = [
    path('', twuser_views.main, name='main'),
    # twUser
    path('join/', twuser_views.join, name='join'),
    path('login/', twuser_views.user_login, name='login'),
    path('activate/<str:uidb64>/<str:token>/', twuser_views.activate, name='activate'),
    path('logout/', twuser_views.logout, name='logout'),
    path('profile/<str:id>', twuser_views.profile, name='profile'),
    path('setting/profile', twuser_views.edit_profile, name='edit_profile'),

    # twTweet
    path('home/', twtweet_views.get_list, name='home'),
    path('tweet/', twtweet_views.tweet, name='tweet'),
    path('update/<int:id>/', twtweet_views.update, name='update'),
    path('delete/<int:id>/', twtweet_views.delete, name='delete'),




]

app_name = 'twc'

