from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Book
from .forms import BookForm

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book.html'
    success_url = reverse_lazy('create_book') 
