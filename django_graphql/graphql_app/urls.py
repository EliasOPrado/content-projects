from django.urls import path
from .views import BookCreateView

from graphene_django.views import GraphQLView

urlpatterns = [
    path('create/', BookCreateView.as_view(), name='create_book'),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]