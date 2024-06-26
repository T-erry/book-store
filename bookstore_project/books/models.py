from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
     return self.name

class Book(models.Model):
    title = models.CharField(max_length=25 ,null=True)
    pageCount = models.IntegerField(default=0)
    shortDescription = models.CharField(max_length=256, null=True)
    longDescription = models.TextField(null=True)
    authors = models.ManyToManyField(Author)
    image = models.ImageField(upload_to="images", null=True)


def __str__(self):
    return self.title

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete= models.CASCADE, null=True)
    image = models.ImageField(upload_to="images/review", null=True)
    
   

