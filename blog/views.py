from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post


class BlogListView(ListView):
    """
    ListView will give us access to object_list whuchcontains all the objects in this view
    It will be used in the home.html to iterate through all blog post of the Post model
    """
    model = Post # model for the view
    template_name = 'home.html' # html we want to render


class BlogDetailView(DetailView): 
    """
    By default, DetailView will provide a context object we can use in our
    template called either 'object' or the lowercased name of our model, which would be 'post'.

    This context obhect helps us to access the data in our model
    """
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView): 
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView): 
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    # reverse_lazy ensures post is deleted before it redirects to home page
    success_url = reverse_lazy('home')
