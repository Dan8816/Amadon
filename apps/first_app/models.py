from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Product(models.Model):
    item = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    item_count = models.IntegerField(default=0)
    def __repr__(self):
        return "<item: {} | {}, {} >".format(self.id, self.item, self.price)


