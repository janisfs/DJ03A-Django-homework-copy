from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'myproject/index.html')

def page1(request):
    return render(request, 'myproject/about.html')

def page2(request):
    return render(request, 'myproject/service.html')

def page3(request):
    return render(request, 'myproject/products.html')

def page4(request):
    return render(request, 'myproject/contacts.html')
