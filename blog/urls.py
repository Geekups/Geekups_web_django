from django.urls import path
from .views import HomePage,AboutUs,Services,Contact,blogs,portfolio


urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('about/',AboutUs.as_view(),name='about'),
    path('services/',Services.as_view(),name='services'),
    path('contact/',Contact.as_view(),name='contact'),
    path('portfolio/',portfolio,name='portfolio'),
    path('blog/',blogs,name='blog'),
]
