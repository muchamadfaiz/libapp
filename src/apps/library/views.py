from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def book_list(request):
    return HttpResponse("ok")
