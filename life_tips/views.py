from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Post

class SustainableTips(ListView):
    model = Post
    template_name = "life_tips/tips.html"

class TipCreateView(CreateView):
    model = Post
    template_name = "life_tips/post_new.html"
    fields = ["text"]