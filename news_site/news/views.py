from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    articles = Article.objects.all
    return render(request, 'index.html', {'articles': articles})


def about(request):
    return render(request, 'about.html')


def story(request):
    return render(request, 'story.html')
