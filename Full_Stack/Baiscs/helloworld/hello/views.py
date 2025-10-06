from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render (request, 'hello/home.html')
    # return HttpResponse("Hello world!")