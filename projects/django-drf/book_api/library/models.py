from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    summary = models.TextField(blank=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return f"{self.title} by {self.author}"
