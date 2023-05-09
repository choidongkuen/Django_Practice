# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from board.models import Question


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
    return HttpResponse("vote 입니다.")


def results(request, board_id):
    return HttpResponse("result 입니다.")
