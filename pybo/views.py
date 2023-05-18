from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from pybo.models import Question
from .forms import QuestionForm, AnswerForm


# Question 모델 데이터 작성한 날짜의 역순(내림 차순) 으로 조회
def index(request):
    page = request.GET.get('page', '1')
    question_list = Question.objects.all().order_by('-created_at')
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {"question_list": page_obj}
    return render(request, "pybo/index.html", context)


# Question 모델 데이터 detail
def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, "pybo/detail.html", {"question": question})


# 답변 등록
@login_required(login_url='common:login')  # 로그인이 안된 상태라면 자동으로 로그인 화면으로 이동
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # request.user => 현재 로그인한 계정의 User 모델 객체
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)  # Question detail 페이지
    else:
        form = AnswerForm()
    context = {"question": question, "form": form}
    return render(request, "pybo/detail.html", context)


# 질문 등록
@login_required(login_url='common:login')
def question_create(request):
    # 저장하기 누른 경우
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # request.user => 현재 로그인한 계정의 User 모델 객체
            question.save()
            return redirect('pybo:index')

    # index.html 에서 질문 등록하기 누른 경우
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


# 질문 수정
@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.user != question.author:  # 요청한 user 와 해당 question author 다르면
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


# 질문 삭제
@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('pybo:detail', question_id=question.id)

    question.delete()
    return redirect('pybo:detail')
