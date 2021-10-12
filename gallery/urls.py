from django.urls.conf import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.photos, name='photos'),
    path('search/', views.search_images, name="search_images"),
    path('category/<category>', views.view_category, name='view_category'),
]
