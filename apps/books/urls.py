from django.urls import path

from apps.books.views import BookViewSet

app_name = "books"

urlpatterns = [
    path("books", BookViewSet.as_view({"get": "list"}), name="book-list"),
    path(
        "books/<id>",
        BookViewSet.as_view({"get": "retrieve", "patch": "partial_update"}),
        name="book-detail",
    ),
]
