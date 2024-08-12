from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book
from .forms import BookForm

# Create your views here.


def book_list(request):
    return render(request, 'book_list.html', {'books': Book.objects.all()})


def book_detail(request, book_id):
    return render(request, 'book_detail.html', {'book': Book.objects.get(id=book_id)})


def book_create_update(request, book_id=None):
    if book_id:
        obj = get_object_or_404(Book, id=book_id)

        form = BookForm(request.POST or None, instance=obj)
        context = dict()
        # save the data from the form and
        # redirect to detail_view
        if form.is_valid():
            form.save()
            return redirect('book_list')

        # add form dictionary to context
        context["form"] = form

        return render(request, "book_form.html", context)
    else:
        book = None

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'book_form.html', {'form': form})




