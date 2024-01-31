from django.urls import path
from multi_tenant.views import home

urlpatterns = [
    path("", home, name='home'),
]