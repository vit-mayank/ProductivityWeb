from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Main(request):
    return render(request,"practice1/home.html")