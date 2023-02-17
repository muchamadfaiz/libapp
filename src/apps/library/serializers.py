from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    author = serializers.CharField()
    quantity = serializers.IntegerField()

