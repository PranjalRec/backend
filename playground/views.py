from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_ashva(request):
    return HttpResponse('Welcome to Ashva!')

def say_ashva_page(request):
    return render(request, 'hello.html')
