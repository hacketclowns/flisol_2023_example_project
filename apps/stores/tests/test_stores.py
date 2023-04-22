from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.books.models import Book
from apps.stores.models import Store
from testing import factories


class StoreBaseTests(TestCase):
    def setUp(self):
        self.app = APIClient()
        self.url = reverse("stores:store-list")

    def _validate_store_response(self, data, store: Store):
        self.assertIsInstance(data, dict)
        self.assertEqual(data.pop("id", None), store.pk)
        self.assertEqual(data.pop("name", None), store.name)
        self.assertEqual(data.pop("location", None), store.location)
        self.assertEqual(data.pop("is_open", None), store.is_open)
        self.assertEqual(data.pop("created_at", None), store.created_at.isoformat().replace("+00:00", "Z"))
        for data, book in zip(data.pop("books", None), store.books.all()):
            self._validate_short_book_response(data, book)
        self.assertFalse(data)

    def _validate_short_book_response(self, data, book: Book):
        self.assertIsInstance(data, dict)
        self.assertEqual(data.pop("title", None), book.title)
        self.assertEqual(data.pop("type", None), book.type)
        self.assertFalse(data)


class StoreListTests(StoreBaseTests):
    pass

