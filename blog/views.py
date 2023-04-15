from django.views.generic import TemplateView

# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'
    
    
class AboutUs(TemplateView):
    template_name = 'abuot.html'

class Services(TemplateView):
    template_name = 'services.html'