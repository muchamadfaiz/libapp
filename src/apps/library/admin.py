from django.contrib import admin
from .models import AuthorModel, CategoryModel, BookModel
# Register your models here.

class Author(admin.ModelAdmin):
    pass
class Category(admin.ModelAdmin):
    pass
class Book(admin.ModelAdmin):
    pass

admin.site.register(AuthorModel, Author)
admin.site.register(CategoryModel, Category)
admin.site.register(BookModel, Book)

