from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from.models import Article, Portfolio,Contact
from .form import ContactForm

# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'
    
    
class AboutUs(TemplateView):
    template_name = 'abuot.html'



#our servieces
class Services(TemplateView):
    template_name = 'services.html'



#send message to us
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            Contact.objects.create(name=name, email=email, text=text)
            return redirect('communication')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})




#نمونه کارا
def portfolio (request):
    portfolio = Portfolio.objects.all()
    context = {
        'portfolio':portfolio
    }
    return render(request,'portfolio.html',context)
    

#website articles
def blogs (request):
    blogs = Article.objects.filter(publish=True)
    context = {
        'blogs':blogs
    }
    return render(request,'blog.html',context)



#when comment saved
class Communication(TemplateView):
    template_name = 'communication.html'
