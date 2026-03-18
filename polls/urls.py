from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("test/", views.test),
    path("create/", views.create_account), 
    path("acc/", views.get_accounts ),
    path("acc/<int:id>/", views.get_account),
    path("acc/<int:id>/update/", views.update_account),
    path("acc/<int:id>/delete/", views.delete_account)
]