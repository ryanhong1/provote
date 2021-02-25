from django.shortcuts import render


def homeview(request):
    return render(request, "index.html")

def aboutview(request):
    return render(request, "about.html")

def votesview(request):
    
    return render(request, "blog.html")

def contactview(request):
    return render(request, "contact.html")

def LoginPageView(request):
    return render(request, "login.html")