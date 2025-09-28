# api/urls.py
from django.urls import path
from django.http import HttpResponse
from .views import BookList, BookDetail

def api_home(request):
    return HttpResponse("API Home")

urlpatterns = [
    path('', api_home),
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]
