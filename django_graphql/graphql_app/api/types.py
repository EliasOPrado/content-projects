import graphene
from graphene_django import DjangoObjectType
from graphql_app.models import Book
from django.contrib.auth.models  import User

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = "__all__"

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"