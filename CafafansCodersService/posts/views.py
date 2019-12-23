from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    posts = {
        'posts': Post.objects.all(),
        'title': 'Main Posts'
    }
    return render(request, 'posts/index.html', posts)