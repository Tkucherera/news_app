from django.shortcuts import render
from .models import *
import math


# Create your views here.
def index(request):
    articles = Articles.objects.all
    return render(request, 'index.html', {'articles': articles})


def about(request):
    return render(request, 'about.html')


def story(request):
    if request.method == 'GET':
        value = int(request.GET.get('value'))
        print(value)
        article = Articles.objects.get(id=value)
        return render(request, 'story.html', {'article': article})

    elif request.method == 'POST':
        article_id = request.POST['article']
        rating = int(request.POST['rating'])
        # get the article in question
        article = Articles.objects.get(id=article_id)
        # prepare to calculate and add new rating
        article_num_ratings = int(article.num_ratings)
        article_old_rating = float(article.rating)
        article_new_num_ratings = article_num_ratings + 1
        article_new_rating = ((article_num_ratings*article_old_rating) + rating) / article_new_num_ratings
        # get writer
        writer_name = article.writer.name
        writer = Writer.objects.get(name=writer_name)
        # calculate new rating for writer
        writer_num_ratings = int(writer.num_ratings)
        writer_old_rating = float(writer.rating)
        writer_new_num_ratings = writer_num_ratings + 1
        writer_new_rating = ((writer_num_ratings * writer_old_rating) + rating) / writer_new_num_ratings
        print('thiss', writer_new_rating)
        # save changes
        article.rating = article_new_rating
        article.num_ratings = article_new_num_ratings
        article.save()
        writer.rating = writer_new_rating
        writer.num_ratings = writer_new_num_ratings
        writer.save()

        return render(request, 'index.html')

    else:
        return render(request, 'index.html')






