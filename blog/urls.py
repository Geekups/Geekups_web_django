from django.urls import path
from .views import HomePage,AboutUs


urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('about/',AboutUs.as_view(),name='about'),

]
