from django.urls import path

from board import views

urlpatterns = [
    path("", views.index(), name="index"),
    path("<int:board_id>/", views.detail(), name="detail"),
    path("<int:board_id>/vote/", views.vote(), name="vote"),
    path("<int:board_id>/results/", views.results(), name="results")
]
