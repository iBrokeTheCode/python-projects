from django.urls import path

from library import views

app_name = "library"

urlpatterns = [
    path("books/", views.BookListCreateView.as_view(), name="book-list"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book-detail"),
    path("books/create/", views.BookCreateView.as_view(), name="book-create"),
]
