from django.shortcuts import render, HttpResponse
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    template = 'blog/post/list.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)
