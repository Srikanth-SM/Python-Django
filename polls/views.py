from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Question, Choice
# Create your views here.

def index(request):
    # return HttpResponse("Polls App")
    return render(request,"index.html",context={'name':'srikanth'})

def details(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
        # print((questions_list[0].choice_set))
        # return HttpResponse("You're looking at question %s." % question_id)
        
    except Exception as e:
        print (e)
        print (dir(e))
        raise Http404(e)
    return render(request,"polls/details.html",context={'question':question})

    

def results(request,question_id):
    return HttpResponse("You are looking at results of question %s."%question_id)

def votes(request,question_id):
    return HttpResponse("U are votng on question id %s."%question_id)

    return HttpResponse("U are votng on question id %s."%question_id)

