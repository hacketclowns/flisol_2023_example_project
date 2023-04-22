from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from testing import factories


from apps.books.models import BookType


class BookBaseTests(TestCase):
    def setUp(self):
        self.app = APIClient()
        self.url = reverse("books:book-list")

    def _validate_short_store_response(self, data, store):
        self.assertIsInstance(data, dict)
        self.assertEqual(data.pop("name", None), store.name)
        self.assertEqual(data.pop("location", None), store.location)

    def _validate_book_response(self, data, book):
        self.assertIsInstance(data, dict)
        self.assertEqual(data.pop("id", None), book.id)
        self.assertEqual(data.pop("title", None), book.title)
        self.assertEqual(
            data.pop(
                "type",
            ),
            book.type,
        )
        self.assertEqual(data.pop("notes", None), book.notes)
        self.assertEqual(
            data.pop("created_at", None),
            book.created_at.isoformat().replace("+00:00", "Z"),
        )
        self._validate_short_store_response(data.pop("selled_by", None), book.selled_by)
        self.assertFalse(data)


class BookListTests(BookBaseTests):
    def setUp(self):
        super().setUp()

    def test_list(self):
        books = factories.Book.create_batch(5)
        books.sort(key=lambda b: b.created_at, reverse=True)
        response = self.app.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], len(books))
        for data, book in zip(response.data["results"], books):
            self._validate_book_response(data, book)

    def test_list__filter_by_family_content(self):
        family_adventure_books = factories.Book.create_batch(3, type=BookType.adventure)
        family_animated_books = factories.Book.create_batch(2, type=BookType.animated)
        factories.Book.create_batch(6, type=BookType.horror)
        all_books = [*family_adventure_books, *family_animated_books]
        all_books.sort(key=lambda b: b.created_at, reverse=True)

        response = self.app.get(self.url, data={"family_friendly": True})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], len(all_books))
        for data, book in zip(response.data["results"], all_books):
            self._validate_book_response(data, book)
