from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    
    path("", views.index , name='home'),
    path("about", views.about , name='about'),
    path("services", views.services , name='services'),
    path("contact", views.contact , name='contact'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contact_list, name='contact_list'),
    path('contact/<int:id>/', views.contact_detail, name='contact_detail'),
    path('contact/<int:id>/edit/', views.contact_edit, name='contact_edit'),
    path('contact/<int:id>/delete/', views.contact_delete, name='contact_delete'),
    
   # path('about/', views.about),
   # path('edit/<int:id>/', views.edit_image),
]