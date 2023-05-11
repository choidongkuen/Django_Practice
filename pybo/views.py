from django.http import HttpResponse

from pybo.models import Question


# Question 모델 데이터 작성한 날짜의 역순(내림 차순) 으로 조회
def index(request):
    question_list = Question.objects.all().order_by('-created_at')
    context = {"question_list", question_list}
    return HttpResponse(request, "pybo/index.html", context)
