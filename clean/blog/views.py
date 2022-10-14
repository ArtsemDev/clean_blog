from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


class Mixin:

    content = {
        'twitter': 'https://twitter.com',
        'facebook': 'https://facebook.com',
        'github': 'https://github.com',
    }


class PostListView(Mixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().order_by('date_created')

    def get_context_data(self, *, object_list=None, **kwargs):
        return super(PostListView, self).get_context_data() | self.content


class PostDetailView(DetailView):
    model = Post
