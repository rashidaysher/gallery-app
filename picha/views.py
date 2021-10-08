from django.shortcuts import render
from django.http  import HttpResponse, Http404

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the kiliga photography')
