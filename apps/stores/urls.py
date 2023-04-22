from django.urls import path

from apps.stores.views import StoreViewSet

app_name = "stores"

urlpatterns = [
    path("stores", StoreViewSet.as_view({"get": "list", "post": "create"}), name="store-list"),
    path("stores/<id>", StoreViewSet.as_view({"get": "retrieve", "patch": "partial_update"}), name="book-detail")
]
