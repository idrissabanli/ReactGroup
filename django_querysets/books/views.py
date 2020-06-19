from django.shortcuts import render
from books.models import Book

def book_list(request):
    search_word = request.GET.get('search')
    print(search_word)
    if search_word:
        book_list = Book.objects.filter(title__contains=search_word)
    else:
        book_list = Book.objects.all()

    context = {
        'books': book_list
    }
    return render(request, 'books.html', context)