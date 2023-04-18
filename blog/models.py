from django.db import models

# Create your models here.

class Article(models.Model):
    title   = models.CharField(max_length=100)
    content = models.TextField()
    publish = models.BooleanField(default=True)
    image   = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    category   = models.CharField(max_length=50)

    def __str__(self):
        return self.title



class Portfolio(models.Model):
    title   = models.CharField(max_length=100)
    content = models.TextField()
    image   = models.ImageField(upload_to='images/')
    category= models.CharField(max_length=50)


class Contact(models.Model):
    email = models.EmailField(max_length=254)
    name  = models.CharField(max_length=50)
    text  = models.TextField()
