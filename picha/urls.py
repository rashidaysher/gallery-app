from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name = 'index'),
    path('search/', views.search_image, name='search_image'),
    path('location/image_location', views.location_filter, name='location_filter'),
    path('image/category_name/image_id',views.single,name = 'single')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)