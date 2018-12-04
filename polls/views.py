from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question, Choice

import json
# Create your views here.


def index(request):
    # return HttpResponse("Polls App")
    questions_list = Question.objects.all()
    return render(
                    request,
                    'polls/index.html',
                    {
                        'questions_list': questions_list
                    }
                 )


def details(request, question_id):
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Exception as e:
    #     print (e)
    #     print (dir(e))
    #     raise Http404(e)
    # return render(request,"polls/details.html",context={'question':question})
    # shortcut to above procedure is using get_object_or_404()
    question = get_object_or_404(Question, pk=question_id)
    question_choices = question.choice_set.all()
    return render(
                    request, 'polls/details.html',
                    {
                        'question': question,
                        'question_choices': question_choices
                    }
                 )


def results(request, question_id):
    # return HttpResponse(
    #                         "You are looking at results of question %s."
    #                         % question_id
    #                    )
    question = Question.objects.get(pk=question_id)
    question_choices = question.choice_set.all()
    print(dir(question), "hai")
    return render(request, "polls/results.html",
                    {
                        'question': question,
                        'choices': question_choices
                    }
                )


def votes(request, question_id):
    # print(dir(request))
    # print(request.body.choice)
    # body_unicode = request
    # print("body_unicode ", body_unicode)
    # body = json.loads(body_unicode)
    # content = body['content']
    # print(dir(Question))
    print(request.POST)
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request, "polls/details.html",
            {
                'question': question,
                'error_message': "YOU did not select a choice"
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect('/polls/'+question_id+'/results/')



