from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()

# register viewset
router.register('books', views.BookViewSet)
router.register('author', views.AuthorViewSet)
router.register('category', views.CategoryViewSet)

urlpatterns = [

] + router.urls