# myapp/views.py
from django.shortcuts import render

def Home(request):
    return render(request, 'page/home.html', {})