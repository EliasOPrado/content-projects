import graphene
from django.contrib.auth.models import User

from graphql_app.models import Book
from graphql_app.api.types import BookType, UserType

class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_users = graphene.List(UserType)
    book_by_title = graphene.Field(BookType, title=graphene.String(required=True))

    def resolve_all_books(root, info):
        return Book.objects.all()

    def resolve_all_users(root, info):
        return User.objects.all()
    
    def resolve_book_by_title(root, info, title):
        try:
            return Book.objects.get(title=title)
        except Book.DoesNotExist:
            return None
    
schema = graphene.Schema(query=Query)