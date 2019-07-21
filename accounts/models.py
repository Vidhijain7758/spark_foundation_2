

from django.db import models

# Create your models here.
class Coffee(models.Model):
    id = models.IntegerField(unique= True,   primary_key = True)
    Coffee_name = models.CharField(max_length =20,default=0)

    Price = models.IntegerField(default=0)


    def __str__(self):
        return "__all__"

