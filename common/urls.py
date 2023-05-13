from django.contrib.auth import views as auth_views
from django.urls import path

app_name = "common"

urlpatterns = [
    # django.contrib.auth 의 LoginView 사용
    path('login/', auth_views.LoginView.as_view(
        # registration login.html 설정 -> common 디렉토리로 변경
        template_name='common/login.html'
    ), name="login")

]
