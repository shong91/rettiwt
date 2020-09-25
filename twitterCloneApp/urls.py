from django.urls import path
from . import views

app_name = 'twc'

urlpatterns = [
    path('', views.main, name='main'),
    path('join/', views.join, name='join'),
    path('login/', views.user_login, name='login'),

]