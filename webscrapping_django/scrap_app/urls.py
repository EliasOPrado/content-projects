from django.urls import path
from .views import my_scraping_view

urlpatterns = [
    path('', my_scraping_view, name='scrapping'),
]