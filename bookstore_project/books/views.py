from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404,redirect
from books.models import Book, Review 
from django.views.generic import ListView, DetailView
from django.core.files.storage import FileSystemStorage
# from django.contrib.auth.mixins import LoginRequiredMixin






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
        #  Creating relationship where Book has many reviews:review_set.all to get all the reviews
        #.order_by('-created_at'): This orders the retrieved reviews by their creation date in descending order (newest first). 
        # This ensures the latest reviews are displayed first.

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
           
            context['reviews'] = context['book'].review_set.order_by('-created_at')
            context['authors'] = context['book'].authors.all()
            return context
            
    
   
# def show(request, id):
    
#     singleBook = get_object_or_404(Book, pk=id)
#     reviews= Review.objects.filter(book_id=id).order_by('-created_at')
#     context = {'book': singleBook, 'reviews':reviews}
#     return render(request, 'books/show.html', context)



def author(request,author):
     books = Book.objects.filter(authors__name=author)
     context ={'book_list': books}
     return render(request, 'books/book_list.html', context)




#POST method
def review(request, id):
    if request.user.is_authenticated:
        image = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save( image.name,image)
   #  create a form instance and populate it with data from the request:
        body = (request.POST['review'])
        newReview = Review(body=body, book_id=id, user=request.user, image=fs.url(name))
        newReview.save()
        return redirect('/books')
    
