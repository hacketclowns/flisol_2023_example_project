from rest_framework import viewsets

from apps.stores.models import Store
from apps.stores.store_serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.all().order_by("-created_at")
