from django.shortcuts import render
from . import models
from django.views.generic import DetailView
# Create your views here.

class PostDetailView(DetailView):
    model = models.Post
