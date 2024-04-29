from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    titulo = forms.CharField(label='Titulo para el post', max_length=250)
    cuerpo = forms.CharField(label='Contenido', widget=forms.Textarea)
    publicado = forms.BooleanField(label='¿Publicar?', required=False)
    
    class Meta:
        model = Post
        fields = ['titulo', 'cuerpo', 'publicado']