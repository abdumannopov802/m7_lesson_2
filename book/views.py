from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Book
from .forms import BookForm

# Create your views here.

class Book_list_view(ListView):
    model = Book
    template_name = 'book-list.html'
    context_object_name = 'books'
    ordering = ['title',]

class Book_detail_view(DetailView):
    model = Book
    template_name = 'book-detail.html'
    context_object_name = 'book'

class Book_create_veiw(CreateView):
    model = Book
    template_name = 'book-create.html'
    fields = '__all__'
    class_form = BookForm
    success_url = reverse_lazy('book-list')

class Book_update_view(UpdateView):
    model = Book
    template_name = 'book-update.html'
    fields = '__all__'
    success_url = reverse_lazy('book-list')

class Book_delete_view(DeleteView):
    model = Book
    pk_url_kwarg = 'pk'
    template_name = 'book-delete.html'
    success_url = reverse_lazy('book-list')
