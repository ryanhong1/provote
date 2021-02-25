from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views.generic import ListView, DetailView
# Create your views here.



class votesView(ListView):

    """ HomeView Definition """

    model = models.Question
    paginate_by = 10
    paginate_orphans = 0
    ordering = "pub_date"
    context_object_name = "questions"

class votesDetailView(DetailView):
    model = models.Question
    

