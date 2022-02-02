from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from . import models
from django.shortcuts import get_object_or_404
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


def vote(request):

    if request.method == "POST":
        c_id = request.POST.get('a')
        c = get_object_or_404(models.Choice, id = c_id)
        c.votes  += 1
        c.save()
        return HttpResponseRedirect(reverse('vote:result',args=(c.q.id ,)  ) )


def result(request, q_id):
    
    return render(request, 'votes/result.html', 
                  {'q' : get_object_or_404(models.Question, id = q_id) } )
    

