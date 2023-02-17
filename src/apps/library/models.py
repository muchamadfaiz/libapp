from django.db import models
class CategoryModel(models.Model):
    name = models.CharField(max_length=100)

class AuthorModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)

class BookModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    