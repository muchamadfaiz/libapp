from django.contrib import admin
from . import models

class BookAdmin(admin.ModelAdmin):
    list_display =  ['title', 'category', 'author', 'quantity', 'price']
    list_editable = ['author','price']
    list_per_page = 10
    ordering = ['-title', '-category']
    
admin.site.register(models.Author)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Category)

