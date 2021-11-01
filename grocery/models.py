from django.db import models

class grocery_store(models.Model):
    ItemID=models.IntegerField()
    Title=models.CharField(max_length=1000)
    Category=models.CharField(max_length=1000)
    class Meta:
        db_table='grocery_store'