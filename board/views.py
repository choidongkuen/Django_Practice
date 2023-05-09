# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("index 입니다.")


def detail(request, board_id):
    return HttpResponse(str(board_id) + "detail 입니다.")


def vote(request, board_id):
    return HttpResponse("vote 입니다.")


def results(request, board_id):
    return HttpResponse("result 입니다.")
