from django.urls.conf import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.photos, name='gallery'),
    path('search/', views.search_images, name="search_images"),
    path('category/<category>', views.view_category, name='view_category'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)