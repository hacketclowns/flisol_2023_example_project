from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from testing import factories


class BookBasetests(TestCase):
    def setUp(self):
        self.app = APIClient()
        self.url = reverse("books:book-list")

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
        self.assertEqual(data.pop("selled_by", None), book.selled_by.id)
        self.assertEqual(
            data.pop("created_at", None),
            book.created_at.isoformat().replace("+00:00", "Z"),
        )
        self.assertFalse(data)


class BookListTests(BookBasetests):
    def setUp(self):
        super().setUp()

    def test_list(self):
        books = factories.Book.create_batch(5)
        books.sort(key=lambda b: b.created_at, reverse=True)
        response = self.app.get(self.url)

        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], len(books))
        for data, book in zip(response.data["results"], books):
            self._validate_book_response(data, book)
