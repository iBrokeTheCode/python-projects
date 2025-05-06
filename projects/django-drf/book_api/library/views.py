from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

from library.filters import BookFilter
from library.models import Book
from library.serializers import BookSerializer

# ================================================================
#                          PAGINATION
# ================================================================


class BookListPNPagination(PageNumberPagination):
    page_size = 3
    page_query_param = "page"
    page_size_query_param = "size"
    max_page_size = 5


class BookListLOPagination(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = "limit"
    offset_query_param = "offset"
    max_limit = 5


# ================================================================
#                              VIEWS
# ================================================================


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter
    pagination_class = BookListPNPagination


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
