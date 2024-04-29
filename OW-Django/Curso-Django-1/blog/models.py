from django.db import models

class Post(models.Model):

    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250) #id que permite encontrar un titulo largo con guiones en lugar de espacios
    cuerpo = models.TextField()
    editor = models.BooleanField(default=False)

    def __str__(self):

        return self.titulo