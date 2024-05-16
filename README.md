#  BookStore application

## Project name

Bookstore - This a Django application that allows users to browse books, view details of individual books, and leave reviews (after logging in). The Django admin interface is used to manage books and reviews (Create, Read, Update, Delete - CRUD).



## Setup
### The first thing to do is to clone the repository:
 - $ git clone git@github.com:T-erry/book-store.git
 -  $ cd book-store


###  Create a virtual environment to install dependencies in and activate it:
- $ virtualenv2 .venv 
- $ source .venv/bin/activate

### Then install the dependencies:
- (env)$ pip install -r requirements.txt

### Once pip has finished downloading the dependencies:
1. (env)$ cd project
2. (env)$ python3 manage.py runserver

And navigate to http://127.0.0.1:8000/books/


## Features
- Users can view a list of all books in the system.
- Users can view details of individual books, including a list of associated reviews.
- Users can search for books by author. 
- Logged-in users can leave reviews for books.

### technologies used
- Django
- SQLite
- HTML
- Tailwind

