from django.db import models
from django.db.models.functions import Length

# models


class Product(models.Model):
    id_product = models.IntegerField(primary_key=True)
    name_product = models.CharField(max_length=200)
    price_product = models.FloatField()
    srock_product = models.IntegerField()

    def __str__(self):
        return self.name_product
