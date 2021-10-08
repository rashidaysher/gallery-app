from re import L
from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404
from .models import Image, Category, Location

# Create your views here.
def index(request):
    images = Image.get_all_images()
    locations = Location.objects.all()
    title = 'Kiliga_photography'

    return render(request, 'index.html', {'title':title, 'images':images, 'locations':locations})
