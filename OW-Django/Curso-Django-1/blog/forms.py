from django import forms

class PostForm(forms.Form):
    titulo = forms.CharField(label='Titulo para el post', max_lenght=250)
    cuerpo = forms.CharField(label='Contenido', max_length=250)
    editor = forms.BooleanField(label='¿Publicar?')