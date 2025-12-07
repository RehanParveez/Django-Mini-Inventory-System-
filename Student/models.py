from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=70)
    quantity = models.IntegerField()
    category = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    

    