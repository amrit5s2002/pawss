from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.About, name='about'),
    path('index/',views.index, name='index'),
]