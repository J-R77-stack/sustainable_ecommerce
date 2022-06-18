from django.urls import path
from . import views

urlpatterns = [
    path('contact_us/', views.contact_view, name='contact'),
    path('contact_us/contact_us', views.contact_view, name='contact_us'),
]
