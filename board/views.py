# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from board.models import Question, Choice


# shortcut -> 단축 함수(내장 함수)


def index(request):
    latest_question_list = Question.objects.all().order_by('-create_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'board/index.html', context)
    # return HttpResponse("index 입니다.")


def detail(request, board_id):
    question = get_object_or_404(Question, pk=board_id)
    return render(request, 'board/detail.html', {"question": question})
    # return HttpResponse(str(board_id) + "detail 입니다.")


def vote(request, board_id):
    p = get_object_or_404(Question, pk=board_id)
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


def results(request, board_id):
    return HttpResponse("result 입니다.")
