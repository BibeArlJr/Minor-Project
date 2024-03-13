from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from .views import home,post,category,about, redirect_to_external_url, search

urlpatterns = [
    path('',home),
    path('Blog/<slug:url>/',post),
    path('category/<slug:url>/',category),
    path('about/',about),
    path('redirect/<int:post_id>/', redirect_to_external_url, name='redirect_to_external_url'),
    path('search/',search),

]

