from django.shortcuts import render

def home(request):
    return render(request, "about/home.html", {})
# Create your views here.

def about(request):
    return render(request, 'about/about.html', {})
