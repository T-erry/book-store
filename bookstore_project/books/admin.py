from django.contrib import admin
from books.models import Book, Author, Review

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title')


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Review)

