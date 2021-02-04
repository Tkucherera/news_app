from django.db import models

# Create your models here.


class Writer(models.Model):
    name = models.CharField(max_length=60)
    about = models.TextField()
    picture = models.ImageField(upload_to='images/')
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    num_articles = models.IntegerField()


class Editor(models.Model):
    name = models.CharField(max_length=60)
    about = models.TextField()
    picture = models.ImageField(upload_to='images/')


class Category(models.Model):
    name = models.CharField(max_length=60)
    num_articles = models.IntegerField(blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True)
    num_ratings = models.IntegerField()
    about = models.TextField()


class Articles(models.Model):
    date = models.DateField()
    time = models.TimeField()
    expiry = models.DateTimeField
    name = models.TextField()
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    story = models.TextField()
    summary = models.CharField(max_length=100, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    num_ratings = models.IntegerField()





# TODO make an algorithm for recommending best content
