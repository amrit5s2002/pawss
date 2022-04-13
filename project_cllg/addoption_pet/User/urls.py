from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('reg/',views.User_reg, name='user_reg'),
    path('login/', views.login, name= 'login'),
    path('logout/',views.log_out ,name='logout'),
    path('profile/',views.profile, name='user_profile'),
]


