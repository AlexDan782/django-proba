from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'book/index.html')

def books(request):
    return render(request, 'book/book_info.html')