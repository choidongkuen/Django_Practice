# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from common.forms import UserForm


def signup(request):
    # 데이터 입력한 후
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # 회원가입이 완료된 이후에 자동으로 로그인 되도록 authenticate & login 함수 사용
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
        # 첫 signup 진입시
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
