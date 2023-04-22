from django.db import models


class BookType(models.TextChoices):
    animated = "animated"
    adventure = "adventure"
    horror = "horror"
    adults = "adults"


class Book(models.Model):
    Type = BookType
    title = models.CharField(max_length=256)
    type = models.CharField(max_length=9, choices=Type.choices)
    notes = models.TextField(blank=True)
    selled_by = models.ForeignKey(
        "stores.Store",
        on_delete=models.PROTECT,
        related_name="books",
    )

    def __str__(self):
        return self.title
