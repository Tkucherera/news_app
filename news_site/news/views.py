from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    articles = Article.objects.all
    return render(request, 'index.html', {'articles': articles})


def about(request):
    return render(request, 'about.html')


def story(request):
    if request.method == 'GET':
        value = int(request.GET.get('value'))
        print(value)
        article = Article.objects.get(id=value)
        return render(request, 'story.html', {'article': article})

    else:
        return render(request, 'index.html')



