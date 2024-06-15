from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from . models import Book,Author,Genre

# # Retrieve all books written by a specific author.

# book_written_by_rabindra = Book.objects.filter(author__name = "rabindranath tagore")
# print(book_written_by_rabindra)

# # Retrieve all authors of a specific genre.

# all_auths_of_comedy = Book.objects.filter(genre__name = "comedy")
# all_auths_of_comedy = [auths.author for auths in all_auths_of_comedy]

# # Add a new book with its corresponding author and genres.

# william = Author.objects.create(name = "william")
# genre = Genre.objects.create(name = "literature")

# new_book = Book.objects.create(title = "williams book",author=william,price = 4321.54)
# new_book.genre.add(genre)

# # update the price of a specific book (here book written having written by william and having genre as literture)
# books = Book.objects.filter(genre__name = "literature",author__name = "williams")

# for book in books:
#     book.price = 543
#     book.save()

# # remove a genre from a book

# book = Book.objects.get(author__name = "williams")
# book.genre.remove(Genre.objects.get(name = "literature"))

## commented the code because they will give error if ran more than once.

class GenreList(View):
    template_name = "book_genre_list.html"
    model = Genre
    def get(self,request,*args,**kwargs):
        all_genres = self.model.objects.all()
        return render(request, self.template_name, {"list_of_genres":all_genres})

class BookDetail(DetailView):
    model = Book
    template_name = "book_detail.html"
    context_object_name = "book"
    
class AuthorDetail(DetailView):
    model = Author
    template_name = "author_detail.html"
    context_object_name = "author"
