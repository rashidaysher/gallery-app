
from django.shortcuts import render
from django.http import Http404
from .models import Location, Category, Image
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def main(request):
    try:
        images = Image.objects.all()
        pic_category = Category.objects.all()
        location = Location.objects.all()
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'index.html', {'images': images, 'pic_category': pic_category, 'location': location})


def search_images(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Image.search_by_category(search_term)
        message = f"{search_term}"
        print(searched_category)

        return render(request, 'search.html', {"message": message, "image": searched_category})

    else:
        message = "Kindly search for any term"
        return render(request, 'search.html', {'message': message})


def view_by_location(request, location):
    try:
        image_location = Image.filter_by_location(location)
        message = location
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'location.html', {"location": image_location, 'message': location})
