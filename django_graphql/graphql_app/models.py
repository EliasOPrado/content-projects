from django.db import models

# Create your models here.
class Book(models.Model):
    GENRE_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Science Fiction', 'Science Fiction'),
        ('Mystery', 'Mystery'),
        ('Fantasy', 'Fantasy'),
        ('Business', 'Business'),
    ]
    title = models.CharField(max_length=120)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    description = models.TextField()
