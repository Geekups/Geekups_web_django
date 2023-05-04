from django.urls import path
from .views import HomePage,AboutUs,Services,contact_view,blogs,portfolio,Communication


urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('about/',AboutUs.as_view(),name='about'),
    path('services/',Services.as_view(),name='services'),
    path('contact/',contact_view,name='contact'),
    path('communication/',Communication.as_view(),name='communication'),
    path('portfolio/',portfolio,name='portfolio'),
    path('blog/',blogs,name='blog'),
]
