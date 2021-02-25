from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('',views.homeview, name = "home"),
    path('about/',views.aboutview, name = "about"),
    path('contact/',views.contactview, name = "contact"),
    path('login/',views.LoginPageView, name = "login"),
   ]    