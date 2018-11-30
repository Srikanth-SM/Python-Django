from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse
from .models import Question, Choice
# Create your views here.

def index(request):
    # return HttpResponse("Polls App")
    return render(request,"index.html",context={'name':'srikanth'})

def details(request, question_id):
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Exception as e:
    #     print (e)
    #     print (dir(e))
    #     raise Http404(e)
    # return render(request,"polls/details.html",context={'question':question})
    
    
    # shortcut to above procedure is using get_object_or_404()
    question = get_object_or_404(Question, pk = question_id)
    return render(request,'polls/details.html', {'question':question}) 
    

def results(request,question_id):
    return HttpResponse("You are looking at results of question %s." %question_id)

def votes(request,question_id):
    return HttpResponse("U are votng on question id %s." %question_id)



