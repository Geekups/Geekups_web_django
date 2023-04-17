from django.urls import path
from .views import HomePage,AboutUs,Services,Contact,Porfolio,blogs


urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('about/',AboutUs.as_view(),name='about'),
    path('services/',Services.as_view(),name='services'),
    path('contact/',Contact.as_view(),name='contact'),
    path('portfolio/',Porfolio.as_view(),name='portfolio'),
    path('blog/',blogs,name='blog'),
]
