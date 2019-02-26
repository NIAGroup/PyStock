from django.http import HttpResponse
from django.shortcuts import render

def home_page_fxn(request):
    #return HttpResponse("Home Page")
    return render(request, 'homepage.html')

def about_page_fxn(request):
    #return HttpResponse("about page")
    return render(request, 'about.html')

