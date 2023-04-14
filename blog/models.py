from django.db import models

# Create your models here.

class Article(models.Model):
    title   = models.CharField(max_length=100)
    content = models.TextField()
    publish = models.BooleanField(default=True)
    image   = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    category   = models.CharField(max_length=50)
