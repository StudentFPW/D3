from .models import Post
from django.views.generic import ListView, DetailView


class NewsList(ListView):
    model = Post
    ordering = 'datetime'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'


class ArticleList(ListView):
    model = Post
    ordering = 'datetime'
    template_name = 'flatpages/articles.html'
    context_object_name = 'article'


class NewsDetail(DetailView):
    model = Post
    template_name = 'flatpages/new.html'
    context_object_name = 'news'


class ArticleDetail(DetailView):
    model = Post
    template_name = 'flatpages/article.html'
    context_object_name = 'article'
