from django.shortcuts import render
from .models import all_users_chat , User, Blog, Report, following,followers

def index(request):
    blog = Blog.objects.all()

    dic = {
        'blog':blog,
    }

    return render(request,'index.html',dic)
