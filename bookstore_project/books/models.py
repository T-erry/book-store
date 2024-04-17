from django.db import models

# Create your models here.

#Book model
class Authors(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=25 ,null=True)
    pageCount = models.IntegerField(default=0)
    thumbnailURL = models.CharField(max_length=256, null=True)
    shortDescription = models.CharField(max_length=256, null=True)
    longDescription = models.TextField(null=True)
    authors = models.ManyToManyField(Authors)


def __str__(self):
    return f"{self.id}{self.title}"

class Review(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete= models.CASCADE, null=True)
    
   

