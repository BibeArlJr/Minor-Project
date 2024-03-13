from django.db import models
from django.utils.html import format_html
from django.urls import reverse
# Create your models here.
#Category Model

class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    url=models.CharField(max_length=100)
    image=models.ImageField(upload_to='category/')


    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px; height:40px;"/>'.format(self.image))

    def __str__(self):
        return self.title

#Post Model

class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content= models.TextField()
    image = models.ImageField(upload_to='post/')
    url = models.SlugField(max_length=100, unique=True)  # Add a SlugField for the URL
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    external_url = models.URLField(null=True,blank=True)  # Add a URL field for external links


    def Pimage_tag(self):
        return format_html('<img src="/media/{}" style="width:40px; height:40px;"/>'.format(self.image))

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'url': self.url})
    






