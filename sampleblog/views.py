# coding=utf-8
from django.views.generic import (ListView, DetailView,
    CreateView, UpdateView, DeleteView)
from django.core.urlresolvers import reverse_lazy

from models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    template_name_suffix = '_create'
    success_url = reverse_lazy('post_list')


class PostUpdateView(UpdateView):
    model = Post
    template_name_suffix = '_update'


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
