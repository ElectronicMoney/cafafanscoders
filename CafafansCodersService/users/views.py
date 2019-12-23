from django.shortcuts import render
from django.http import HttpResponse
# from .models import User

# Create your views here.
# def index(request):
#     users = {
#         'users': User.objects.all()
#     }
#     return render(request, 'home.html', users)

users = [
    {
        'id': 1,
        'name': 'Emeka Augustine',
        'email': 'emoney@gmail.com',
        'username': 'emoney'
    },
    {
        'id': 2,
        'name': 'Tega Ogene',
        'email': 'tega@gmail.com',
        'username': 'tipsy'
    }
]

def users(request):
    users_data = {
        'users': users,
        'title': 'Users Lists'
    }
    # return HttpResponse('<h1>Hello World Users</h1>')
    return render(request, 'users/index.html', users_data)