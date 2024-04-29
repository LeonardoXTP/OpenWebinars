from django.shortcuts import render, HttpResponse
from django.http import Http404
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    template = 'post/lista.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)


def post_detail(request, id):
    template = 'post/detalles.html'
    try:
        post = Post.objects.get(id=id)
        context = {
            'post': post,
        }
    except Post.DoesNotExist:
        raise Http404("Publicación no encontrada")
    
    return render(request, template, context)

