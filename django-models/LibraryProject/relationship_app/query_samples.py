import os 
import django
#setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()
from relationship_app.models import Author, Book, Library, Librarian
#1.Query all books by a specific author 
def get_books_by_author(author_name):
    author = Author.objects.get(name =author_name)
    return author.books.all()
#2 List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name = library_name)
    return library.books.all()
#3 retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name = library_name)
    return library.librarian
if __name__ == "__main__":
    print("Books by John Doe:", list(get_books_by_author("John Doe")))
    print("Books in Central Library:", list(get_books_in_library("Central Library")))
    print("Librarian of Central Library:", get_librarian_for_library("Central Library"))


