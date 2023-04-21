from django.shortcuts import render
from django.views.generic import TemplateView
from.models import Article, Portfolio

# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'
    
    
class AboutUs(TemplateView):
    template_name = 'abuot.html'

class Services(TemplateView):
    template_name = 'services.html'

class Contact(TemplateView):
    template_name = 'contact.html'
    #todo add form for input


def portfolio (request):
    portfolio = Portfolio.objects.all()
    context = {
        'portfolio':portfolio
    }
    return render(request,'portfolio.html',context)
    


def blogs (request):
    blogs = Article.objects.all()
    context = {
        'blogs':blogs
    }
    return render(request,'blog.html',context)

