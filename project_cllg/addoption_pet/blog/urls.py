from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    # UserPostListView,
)
from django.urls import path

urlpatterns = [
    path('home',  PostListView.as_view()  ,name='blog-home'),
    path('detail/<int:pk>/',  PostDetailView.as_view()  ,name='blog-detail'),
    path('create',  PostCreateView.as_view()  ,name='blog-detail'),
    path('delete/<int:pk>/',  PostDeleteView.as_view()  ,name='blog-delete'),
    path('update/<int:pk>/',  PostUpdateView.as_view()  ,name='blog-update'),
    ]