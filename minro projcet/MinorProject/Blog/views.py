from django.shortcuts import render, redirect
from django.http import HttpResponse
from Blog.models import Post,Category
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
def home(request):
    #load all the post from db(20)
    posts = Post.objects.all()
    page_number = request.GET.get('page',1)
    paginator = Paginator(posts,8)
    postsfinal = paginator.get_page(page_number)
    totlapage = postsfinal.paginator.num_pages
    cats = Category.objects.all()
    current_page_number = int(page_number)
    data = {
        'posts': postsfinal,
        'lastpage': totlapage,
        'cats': cats,
        'totalPagelist': [n+1 for n in range(totlapage)],
        'current_page_number': current_page_number
    }
    return render(request, 'home.html', data)

def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request, 'post.html', {'post': post, 'cats':cats})

def redirect_to_external_url(request, post_id):
    post = Post.objects.get(pk=post_id)
    return redirect(post.external_url)

def about(request):
    return render(request,'footer.html',{})

def category(request, url):
    cat=Category.objects.get(url=url)
    posts=Post.objects.filter(category=cat)
    return render(request,"category.html",{'cat':cat,'posts':posts})

def search(request):
    query = request.GET.get('query', '')
    if len(query)>50:
        posts = []
        cats = []
    # posts = Post.objects.all()
    else:
        cats = Category.objects.filter(title__icontains=query)
        poststitle = Post.objects.filter(title__icontains=query)
        postscontent = Post.objects.filter(content__icontains=query)
        posts = poststitle.union(postscontent)
    
    params = {'posts':posts,
              'cats':cats,
              'query':query}
    return render(request,'search.html',params)


