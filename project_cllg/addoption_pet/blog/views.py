from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog-detail.html'
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/blog_form.html'
    fields = ['title', 'content']
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class  PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/blog-delete-confirm.html'
    success_url = '/'
    print("comming")
    def test_func(self):
        post = self.get_object()
        i = False
        if self.request.user == post.author:
            i = True
            return i
        
        print(i)
        return i

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Post
    template_name = 'blog/blog_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False