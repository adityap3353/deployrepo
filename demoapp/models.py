from django.db import models

# Create your models here.


class Customer(models.Model):
    custName = models.CharField(max_length=15)
    custAge = models.IntegerField()
    custBalance = models.IntegerField()

    class Meta:
        db_table = "Customer_Info"

