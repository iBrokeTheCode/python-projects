import django_filters

from library.models import Book


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name="title", lookup_expr="icontains"
    )  # Look for ?title=
    author = django_filters.CharFilter(
        field_name="author", lookup_expr="icontains"
    )  # Look for ?author=
    publication_year = django_filters.NumberFilter(
        field_name="publication_date__year",
        lookup_expr="exact",
    )  # Look for ?publication_year=
    isbn = django_filters.CharFilter(field_name="isbn", lookup_expr="exact")
    has_summary = django_filters.BooleanFilter(
        field_name="summary", lookup_expr="isnull", exclude=True
    )  # Look for ?has_isbn=true (exclude revert the condition)
    has_isbn = django_filters.BooleanFilter(
        field_name="isbn", lookup_expr="isnull", exclude=True
    )  # Look for ?has_isbn=true

    class Meta:
        model = Book
        # fields = ("title", "author") # Default filter is exact
        fields = {
            "publication_date": ("gte", "lte", "range")
        }  # Look for ?publication_date__gte=...&publication_date__lte=... | ?publication_date__range=...,...
