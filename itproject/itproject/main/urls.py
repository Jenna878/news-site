from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), 
    path('about', views.about, name='about'), 
    path('contact', views.contact, name='contact'),
    path('contact_detail', views.contact_detail, name='contact_detail'),  
    path('about_detail', views.about_detail, name='about_detail')  
]