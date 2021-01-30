from django.db import models

# Create your models here.


class Article(models.Model):
    date = models.DateField()
    time = models.TimeField()
    expiry = models.DateTimeField
    name = models.TextField()
    writer = models.CharField(max_length=60)
    editor = models.CharField(max_length=60)
    category = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    story = models.TextField()
    summary = models.CharField(max_length=100, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
