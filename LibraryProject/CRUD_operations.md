frm bookshelf.models import Book 
from bookshelf.models import Book
Book.objects.all()
book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.all()
book.delete()
Book.objects.all()
