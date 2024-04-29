from django.contrib import admin
from .models import Post

# Register your models here.
# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'slug', 'cuerpo', 'editor']
    list_filter = ['editor']
    search_fields = ['titulo', 'cuerpo']
    prepopulated_fields = {'slug': ('titulo',)}