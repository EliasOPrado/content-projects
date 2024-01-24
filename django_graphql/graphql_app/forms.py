from django import forms
from .models import Book
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title', 'placeholder': 'Enter the title'}),
            'author': forms.Select(attrs={'class': 'author'}),
            'genre': forms.Select(attrs={'class': 'genre'}),
            'description': forms.TextInput(attrs={'class': 'description', 'placeholder': 'Add a description'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'