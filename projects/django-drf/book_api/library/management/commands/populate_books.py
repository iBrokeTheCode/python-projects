from datetime import date

from django.core.management.base import BaseCommand

from library.models import Book


class Command(BaseCommand):
    help = "Populates the database with initial book data"

    def handle(self, *args, **options):
        # Clear database
        Book.objects.all().delete()

        # Add some sample records
        Book.objects.create(
            title="The Hitchhiker's Guide to the Galaxy",
            author="Douglas Adams",
            publication_date=date(1979, 10, 12),
            isbn="9780345391803",
            summary="A comedic science fiction adventure.",
        )
        Book.objects.create(
            title="Pride and Prejudice",
            author="Jane Austen",
            publication_date=date(1813, 1, 28),
            summary="A classic novel of manners.",
        )
        Book.objects.create(
            title="To Kill a Mockingbird",
            author="Harper Lee",
            publication_date=date(1960, 7, 11),
            isbn="9780446310789",
            summary="A powerful story about justice and prejudice in the American South.",
        )

        self.stdout.write(
            self.style.SUCCESS("Successfully populated the database with initial books")
        )
