from django.urls import path
from .views import SustainableTips, TipCreateView

urlpatterns = [
    path('life_tips/', SustainableTips.as_view(), name='life_tips'),
    path('post/new/', TipCreateView.as_view(), name='post_new'),
]