from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.

class Politician(models.Model):
    name = models.CharField(max_length=50,default="")
    office = models.CharField(max_length=50,default="")
    party = models.CharField(max_length=50,default="", null=True)
    image_url = models.CharField(max_length=200,default="", null=True)
    phone = models.CharField(max_length=13,default="", null=True)
    address_line_1 = models.CharField(max_length=50,default="", null=True)
    city = models.CharField(max_length=30,default="", null=True)
    state = models.CharField(max_length=2,default="", null=True)
    zip_code = models.CharField(max_length=10,default="", null=True)
    facebook = models.CharField(max_length=50,default="", null=True)
    twitter = models.CharField(max_length=50,default="", null=True)
    youtube = models.CharField(max_length=50, default="", null=True)
    constituent = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True, unique=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return (self.office + " " + self.name)
    
    def get_absolute_url(self):
        return reverse('rep_detail', args=[str(self.id)])

class Article(models.Model):
    title = models.CharField(max_length=100, default="", null=True)
    author = models.CharField(max_length=50, default="", null=True)
    description = models.TextField(default="",null=True)
    url = models.CharField(max_length=100, default="", null=True)
    url_to_image = models.CharField(max_length=100, default="", null=True)
    id = models.AutoField(primary_key=True, unique=True)

class RedditPost(models.Model):
    title = models.CharField(max_length=200, default="")
    thumbnail = models.CharField(max_length=200, default="")
    reddit_url = models.CharField(max_length=200, default="")
    id = models.AutoField(primary_key=True, unique=True)