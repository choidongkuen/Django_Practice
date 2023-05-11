from django.shortcuts import render, get_object_or_404, redirect

from pybo.models import Question
from .forms import QuestionFrom


# Question 모델 데이터 작성한 날짜의 역순(내림 차순) 으로 조회
def index(request):
    question_list = Question.objects.all().order_by('-created_at')
    context = {"question_list": question_list}
    return render(request, "pybo/index.html", context)


# Question 모델 데이터 detail
def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, "pybo/detail.html", {"question": question})


# Answer 모델 등록
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'))
    return redirect('pybo:detail', question_id=question.id)  # detail redirect


# Question 모델 등록
def question_create(request):
    # 저장하기 누른 경우
    if request.method == 'POST':
        form = QuestionFrom(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('pybo:index')

    # index.html 에서 질문 등록하기 누른 경우
    else:
        form = QuestionFrom()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
