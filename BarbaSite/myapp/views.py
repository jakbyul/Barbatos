from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def my_view(request):
    return render(request, 'myapp/my_temp.html')

def my_html(request):
    return HttpResponse("Hello, world. You're at the polls index.")


