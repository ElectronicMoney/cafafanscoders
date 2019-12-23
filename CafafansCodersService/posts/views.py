from django.shortcuts import render
from django.http import HttpResponse
# from .models import User

# Create your views here.
# def index(request):
#     users = {
#         'users': User.objects.all()
#     }
#     return render(request, 'home.html', users)

def index(request):
    return render(request, 'posts/index.html')