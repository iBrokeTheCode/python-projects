from django.urls import path

from library import views

app_name = "library"

urlpatterns = [
    path("books/", views.BookListCreateAPIView.as_view(), name="books-list-create"),
    path(
        "books/<int:pk>/",
        views.BookRetrieveUpdateDestroyAPIView.as_view(),
        name="books-retrieve-update-delete",
    ),
]
