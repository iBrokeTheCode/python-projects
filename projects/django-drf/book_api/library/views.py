from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from library.filters import BookFilter
from library.models import Book
from library.serializers import BookSerializer

# from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
# from library.throttling import CustomRateThrottle

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
# ADAPTA


class BookListCreateAPIView(generics.ListCreateAPIView):
    # order_by("pk") # Avoid warning for pagination with unordered list
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    filterset_class = BookFilter
    search_fields = ("title", "=author")
    ordering_fields = ("title", "author")

    pagination_class = BookListPNPagination

    permission_classes = (IsAuthenticatedOrReadOnly,)

    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # throttle_classes = (CustomRateThrottle,)
    throttle_scope = "books"


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
