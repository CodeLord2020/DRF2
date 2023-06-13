from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
# Create your views here.

from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer

class BookAPIView(generics.ListAPIView):
    permission_classes =[IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    permission_classes =[IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    lookup_field = 'pk'

class BookRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes =[IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
 