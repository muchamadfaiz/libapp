from decimal import Decimal
from rest_framework import serializers
from .models import Book, Author, Category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id', 'title', 'description', 'author', 'price', 'price_with_tax', 'category'
        ]

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax (self, book:Book):
        return book.price * Decimal(1.1)

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'email']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
    

