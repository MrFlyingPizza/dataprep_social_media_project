from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, 'base.html', {})

def courses_view(request):
    context = { 
        "department": "Computing Science" 
    }
    # passing data
    return render(request, 'courses.html', context)

def library_view(request):
    return render(request, 'library.html', {})