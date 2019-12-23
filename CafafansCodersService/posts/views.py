from django.shortcuts import render
from django.http import HttpResponse
# from .models import User

# Create your views here.
# def index(request):
#     users = {
#         'users': User.objects.all()
#     }
#     return render(request, 'home.html', users)

posts = [
    {
        'id': 1, 
        'author': 'Emeka Augustine', 
        'title': 'First Bog Post',
        'content': 'The first post is so beautiful!',
        'date_posted': 'August 14th, 2019'
    },
    {
        'id': 2, 
        'author': 'Emeka Augustine', 
        'title': 'Second Bog Post',
        'content': 'The second blog post is so beautiful!',
        'date_posted': 'August 24th, 2019'
    }
]

def index(request):
    posts_data = {
        'posts': posts
    }
    return render(request, 'posts/index.html', posts_data)