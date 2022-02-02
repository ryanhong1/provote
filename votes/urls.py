from django.urls import path
from . import views

app_name = "votes"

urlpatterns = [
    path('',views.votesView.as_view(), name = "list"),
    path("<int:pk>/", views.votesDetailView.as_view(), name="detail"),
    path('<int:pk>/result/', views.result, name='result'),
    path('<int:pk>/vote', views.vote, name='vote'),
   ]   