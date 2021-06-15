from django.shortcuts import render,get_object_or_404

from .models import Article,Category
def category(request,slug):
    context= {
        "category":get_object_or_404(Category,slug=slug,status=True)
    }
    return render(request,"blog/post.html",context)
  
# Create your views here.

def index(request):
    context = {
        #gets all published('p') articles and order the by published date
        "articles":Article.objects.filter(status='p').order_by('-publish'),
        "category":Category.objects.filter(status=True)

    }
    return render(request,"blog/index.html",context)

def post(request,slug):
    context={
        "article":get_object_or_404(Article,slug=slug,status='p')
    }
    return render(request,"blog/post.html",context)