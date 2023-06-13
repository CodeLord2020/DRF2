from rest_framework import serializers
from books.models import Book, Todo


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id","title", "subtitle", "genre" , "author", "isbn")

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
