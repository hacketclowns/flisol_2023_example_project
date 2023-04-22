from django.db import models


class BookType(models.TextChoices):
    animated = "animated"
    adventure = "adventure"
    horror = "horror"
    adults = "adults"


class BookQuerySet(models.QuerySet):
    def family_friendly(self):
        return self.filter(
            type__in=[BookType.adventure, BookType.animated]
        )


class Book(models.Model):
    Type = BookType
    objects = BookQuerySet.as_manager()

    title = models.CharField(max_length=256)
    type = models.CharField(max_length=9, choices=Type.choices)
    notes = models.TextField(blank=True)
    selled_by = models.ForeignKey(
        "stores.Store",
        on_delete=models.PROTECT,
        related_name="books",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
