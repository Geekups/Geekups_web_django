from django.db import models

# Create your models here.

class Article(models.Model):
    title   = models.CharField(max_length=100, verbose_name="عنوان")
    content = models.TextField(verbose_name="محتوا")
    publish = models.BooleanField(default=True, verbose_name="انتشار")
    image   = models.ImageField(upload_to='images/', verbose_name="عکس")
    created_at = models.DateTimeField(auto_now_add=True)
    category   = models.CharField(max_length=50, verbose_name="دسته بندی")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها"



class Portfolio(models.Model):
    title   = models.CharField(max_length=100, verbose_name="عنوان")
    content = models.TextField(verbose_name="محتوا")
    image   = models.ImageField(upload_to='images/', verbose_name="عکس")
    category= models.CharField(max_length=50, verbose_name="دسته بندی")
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "نمونه کار"
        verbose_name_plural = "نمونه کار ها"


class Contact(models.Model):
    email = models.EmailField(max_length=254, verbose_name="ایمیل")
    name  = models.CharField(max_length=50, verbose_name="نام")
    text  = models.TextField(verbose_name="متن")
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "تماس"
        verbose_name_plural = "تماس ها"