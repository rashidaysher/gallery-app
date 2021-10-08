from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name = 'index'),
    path('search/', views.search_image, name='search_image'),
    path('location/(?P<image_location>\d+)', views.location_filter, name='location_filter'),
    path('image/(?P<category_name>\w+)/(?P<image_id>\d+)',views.single,name = 'single')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)