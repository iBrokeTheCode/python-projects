import django_filters

from library.models import Book


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    author = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Book
        fields = ("title", "author")
        # fields = ("title", "author") # Default filter is exact
        # fields = {"title": ["icontains", "iexact"], "author": ["icontains", "iexact"]} # Apply many filters to a field
