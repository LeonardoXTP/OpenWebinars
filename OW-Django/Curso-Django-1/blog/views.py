from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.http import Http404
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(publicado=True)
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


def create_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            post = form.save()
            messages.success(request, 'El post se creó con éxito, felicidades ;)')
            return render(request, 'post/crearpost.html', {'new_post': post})
    else:
        form = PostForm()

    context = {
        'form': form
    }

    return (render(request, 'post/crearpost.html', context))