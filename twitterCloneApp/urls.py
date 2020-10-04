from django.urls import path
from . import views

app_name = 'twc'

urlpatterns = [
    path('', views.main, name='main'),
    # join/login
    path('join/', views.join, name='join'),
    path('login/', views.user_login, name='login'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('logout/', views.logout, name='logout'),

    # tweet CRUD
    path('home/', views.list, name='home'),
    path('tweet/', views.tweet, name='tweet'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),


]