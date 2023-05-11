from django.shortcuts import render

from pybo.models import Question


# Question 모델 데이터 작성한 날짜의 역순(내림 차순) 으로 조회
def index(request):
    question_list = Question.objects.all().order_by('-created_at')
    context = {"question_list": question_list}
    return render(request, "pybo/index.html", context)


def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, "pybo/detail.html", {"question": question})
