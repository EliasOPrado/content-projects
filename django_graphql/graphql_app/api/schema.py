import graphene
from graphene_django import DjangoObjectType

from graphql_app.models import Book
from django.contrib.auth.models import User

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = "__all__"

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"

class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    book_by_title = graphene.Field(BookType, title=graphene.String(required=True))

    all_users = graphene.List(UserType)

    def resolve_all_books(root, info):
        return Book.objects.all()

    def resolve_book_by_title(root, info, title):
        try:
            return Book.objects.get(title=title)
        except Book.DoesNotExist:
            return None
        
    def resolve_all_users(root, info):
        return User.objects.all()


schema = graphene.Schema(query=Query)