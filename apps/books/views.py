from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as djfilters

from apps.books.models import Book
from apps.books.filters import BookFilterSet
from apps.books.book_serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("-created_at")
    serializer_class = BookSerializer
    filter_backends = (
        djfilters.DjangoFilterBackend,
    )
    filterset_class = BookFilterSet
