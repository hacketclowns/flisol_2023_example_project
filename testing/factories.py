import factory
from factory.django import DjangoModelFactory

from apps.books.models import BookType
from apps.stores.models import Location


class Store(DjangoModelFactory):
    class Meta:
        model = "stores.Store"

    name = factory.Sequence(lambda n: f"Store {n}")
    location = Location.undefined


class Book(DjangoModelFactory):
    class Meta:
        model = "books.Book"

    title = factory.Sequence(lambda n: f"Tittle {n}")
    type = BookType.adventure
    selled_by = factory.SubFactory(Store)
