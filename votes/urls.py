from django.urls import path
from . import views

app_name = "votes"

urlpatterns = [
    path('',views.votesView.as_view(), name = "list"),
    path("<int:pk>/", views.votesDetailView.as_view(), name="detail"),
   ]   