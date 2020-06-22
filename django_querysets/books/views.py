from django.shortcuts import render
from books.models import Book, Author
from django.db.models import Q
import math

def book_list(request):
    print(request.GET)
    # {
    #     'search': 'kitab',
    #     'author': 'Tural'
    # }
    # http://localhost:8000/books/?search=Kitab&author=Senan
    search_word = request.GET.get('search')
    print(search_word)
    author_name = request.GET.get('author')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    page = int(request.GET.get('page', 1))
    authors = Author.objects.all()
    search_dict = {}
    last_search = request.get_full_path()
    
    # print(last_search)
    if search_word:
        search_dict['title__contains'] = search_word
    if author_name and author_name != '0':
        search_dict['author__full_name'] = author_name
    if min_price:
        search_dict['price__gt'] = min_price # Book.objects.filter(price__gte=min_price)
    if max_price:
        search_dict['price__lt'] = max_price # Book.objects.filter(price__lte=max_price)
    
    # book_list = Book.objects.filter(title__contains=search_word, author__full_name=author_name, price__lte=max_price, price__gte=min_price)
    book_list = Book.objects.filter(**search_dict)[(page-1)*3:page*3]
    # a = [1,2,3,4,5]
    # a[0:3]
    # a[3:6]
    # a[6:9]
    page_count = math.ceil(Book.objects.filter(**search_dict).count()/3) # 2
    page_range = range(1, page_count+1) # [1,2]
    print(book_list.query)
    context = {
        'books': book_list,
        'author_list': authors,
        'page_range': page_range,
        'last_search': last_search
        
    }
    return render(request, 'books.html', context)