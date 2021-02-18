from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('',views.homeview, name = "home"),
    path('about/',views.aboutview, name = "about"),
   ]    