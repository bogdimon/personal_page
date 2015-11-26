from django.db import models

# Create your models here.
class Item(models.Model):
    publish_date = models.DateField(max_length=200)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    # author_email = models.Char
    text = models.TextField()#CharField(max_length=1000)
    url = models.URLField()
    thumbnail = models.CharField(max_length=200)