from rest_framework import serializers

from apps.books.book_serializers import ShortBookSerializer
from apps.stores.models import Store





class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields: tuple[str, ...] = (
            "id",
            "name",
            "location",
            "is_open",
            "created_at",
            "books",
        )

    books = ShortBookSerializer(many=True)
