# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from board.models import Question, Choice


# shortcut -> 단축 함수(내장 함수)


# index : main
def index(request):
    latest_question_list = Question.objects.all().order_by('-create_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'board/index.html', context)
    # return HttpResponse("index 입니다.")


# detail : question_id 에 맞는 question 상세
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'board/detail.html', {"question": question})
    # return HttpResponse(str(question_id) + "detail 입니다.")


# vote : question_id 에 
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'board/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice[plz click any choice you want]",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('board:results', args=(p.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'board/results.html', {"question": question})
    # return HttpResponse("result 입니다.")
