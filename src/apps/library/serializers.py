from decimal import Decimal
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    author = serializers.CharField()
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax (self, book:Book):
        return book.price * Decimal(1.1)

