from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def VotesView(request): 
    all_votes = models.Question.objects.all()
    return render(request, "indexx.html", {"all_votes":all_votes})