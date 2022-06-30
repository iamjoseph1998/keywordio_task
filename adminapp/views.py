from django.shortcuts import render, redirect
from .models import Book

# Create your views here.
def home(request):
    books_data = Book.objects.all()
    context = {'books_data': books_data}
    return render(request, 'home.html', context=context)

def addbook(request):
    if request.method == 'POST':
        #Get form values
        book_name = request.POST['book_name']
        author = request.POST['author']
        quantity = request.POST['quantity']

        if Book.objects.filter(book_name=book_name, author=author).exists():
            print('Book already exist')
            return redirect('adminapp:addbook')
        else:
            book = Book(book_name=book_name, author=author, quantity=quantity)
            book.save()
            print('Book added successfully')
            return redirect('adminapp:home')
    else:
        return render(request, 'addbook.html')

def updatebook(request):
    books_data = Book.objects.all()
    context = {'books_data': books_data}

    #Fetch book record
    if request.method == 'GET':
        id = request.GET['id']
        book = Book.objects.get(id=id)
        context = {'book': book}
        return render(request, 'updatebook.html', context=context)
    elif request.method == 'POST': #update record
        book_name = request.POST['book_name']
        author = request.POST['author']
        quantity = request.POST['quantity']
        if book_name != '' and book_name != book.book_name:
            book.book_name = book_name
            book.save()

        if author != '' and author != book.author:
            book.author = author
            book.save()

        if quantity != 0 and quantity != book.quantity:
            book.quantity = quantity
            book.save()
        else:
            return redirect('adminapp:home')
    else: 
        return render(request, 'updatebook.html', context=context)

def deletebook(request):
    if request.method == 'POST':
        id = request.POST['id']
        if Book.objects.filter(id=id).exists():
            book = Book.objects.get(id=id)
            book.delete()
            print('Record deleted')
            return redirect('adminapp:home')
        else:
            print('Incorrect ID')
            return redirect('adminapp:deletebook')
    else:    
        return render(request, 'deletebook.html')