from django.urls import path
from django.conf import settings
from .views import my_scraping_view
from django.conf.urls.static import static

urlpatterns = [
    path('', my_scraping_view, name='scrapping'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)