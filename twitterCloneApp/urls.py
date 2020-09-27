from django.urls import path
from . import views

app_name = 'twc'

urlpatterns = [
    path('', views.main, name='main'),
    path('join/', views.join, name='join'),
    path('login/', views.user_login, name='login'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('home/', views.get_list, name='home'),
    path('tweet/', views.tweet, name='tweet')

]