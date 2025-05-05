from django.urls import path

from library import views

app_name = "library"

urlpatterns = [
    path("books/", views.BookList.as_view(), name="book-list"),
    path("books/<int:pk>/", views.BookDetail.as_view(), name="book-details"),
]
