from django.db import models



class Location(models.TextChoices):
    central = "central zone"
    south = "south zone"
    countryside = "rural zone"
    undefined = "unknown"

 
class Store(models.Model):
    StoreLocation = Location

    name = models.CharField(max_length=20, blank=False)
    location = models.CharField(max_length=12, choices=StoreLocation.choices, default=StoreLocation.undefined)
    is_open = models.BooleanField(default=False)
