from django.contrib import admin
from .models import Category, Post


# Register your models here.

# from configuration of category admin.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("image_tag","title",)
    search_fields = ("title",)
    list_filter = ("title",)
    list_per_page = 15


class PostAdmin(admin.ModelAdmin):
    list_display = ("Pimage_tag","title",)
    search_fields = ("title",)
    list_filter = ("category","title")
    list_per_page = 15

    class Media:
        js=('https://cdn.tiny.cloud/1/2fuaivnkx6y4yf9nkcw7fe2xk74mtmnbh1ef8d0weo1dw6r8/tinymce/5/tinymce.min.js','js/script.js')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
