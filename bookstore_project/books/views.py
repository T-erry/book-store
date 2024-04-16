from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404,redirect

from books.models import Book, Review 
from django.views.generic import ListView, DetailView





# Create your views here.
class BookListView(ListView):

    def get_queryset(self):
        return Book.objects.all()


# def index(request):
#     dbData = 
#     context_object_name = {'books': dbData}

#     return render(request, 'books/index.html', context)
class BookDetailView(DetailView):
    model = Book
     #.review_set: This accesses the related manager for the review field (assuming a foreign key relationship between Book and Review models).
        #  Creating relationship where Book has many reviews:book.review_set.all to get all the reviews
        #.order_by('-created_at'): This orders the retrieved reviews by their creation date in descending order (newest first). 
        # This ensures the latest reviews are displayed first.

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
           
            context['reviews'] = context['book'].review_set.order_by('-created_at')
            return context
            
    
   
# def show(request, id):
    
#     singleBook = get_object_or_404(Book, pk=id)
#     reviews= Review.objects.filter(book_id=id).order_by('-created_at')
#     context = {'book': singleBook, 'reviews':reviews}
#     return render(request, 'books/show.html', context)


#POST method
def review(request, id):
   # # create a form instance and populate it with data from the request:
   body = (request.POST['review'])
   newReview = Review(body=body, book_id=id)
   newReview.save()
   return redirect('/books')
    