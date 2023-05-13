from django.urls import path

from board import views

app_name = "board"

urlpatterns = [
    path("", views.index, name="index"),  # "board/"
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("<int:question_id>/results/", views.results, name="results")
]
