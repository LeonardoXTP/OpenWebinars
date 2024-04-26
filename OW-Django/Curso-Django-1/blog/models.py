from django.db import models

class Post(models.Model):

    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250) #id que permite encontrar un titulo largo con guiones en lugar de espacios
    body = models.TextField()
    publisher = models.BooleanField(default=False)

# Create your models here.
