from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book
from datetime import datetime



def books_view(request, date=None):
    template = 'books/books_list.html'
    books = Book.objects.all()
    next_date, prev_date = None, None
    if date:
        date = datetime.strptime(date, '%Y-%m-%d')
        books_by_date = books.filter(pub_date=date)
        next_book = books.filter(pub_date__gt=date).order_by('pub_date').first()
        if next_book:
            next_date = datetime.strftime(next_book.pub_date, '%Y-%m-%d')
        prev_book = books.filter(pub_date__lt=date).order_by('-pub_date').first()
        if prev_book:
            prev_date = datetime.strftime(prev_book.pub_date, '%Y-%m-%d')
        books = books_by_date
    context = {'books': books,
               'prev_date': prev_date,
               'next_date': next_date}
    return render(request, template, context)
