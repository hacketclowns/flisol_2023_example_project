from rest_framework import serializers

from apps.books.models import Book
from apps.stores.models import Store


class ShortStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields: tuple[str, ...] = (
            "name",
            "location",
        )


class ShortBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields: tuple[str, ...] = (
            "title",
            "type",
        )


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    selled_by = ShortStoreSerializer()
