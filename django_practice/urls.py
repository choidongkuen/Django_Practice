"""
URL configuration for django_practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Homehttps://github.com/choidongkuen/Django_Practice.git
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# /board/ -> index() -> index.html
# /board/5/ -> detail()[5번의 detail] -> detail.html
# /board/5/vote/ -> vote()[5번 vote] -> detail.html 넘어온 post 처리
# /board/5/results/ -> results()[5번 vote 수 결과] -> result.html
# /admin/ -> admin 기능

urlpatterns = [
    path("admin/", admin.site.urls),
    path("board/", include("board.urls")),
    path("pybo/", include("pybo.urls")),
    path("common/", include("common.urls"))
]
