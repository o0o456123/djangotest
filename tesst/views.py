from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def add(request):
    a = request.GET["a"]
    b = request.GET["b"]
    c = int(a)+int(b)
    return HttpResponse(str(c))