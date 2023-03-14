# from django.db import models

# # Create your models here.
# class crud_student(models.Model):
#     name = models.CharField(max_length=40)
#     email = models.EmailField(max_length=40)
#     address = models.CharField(max_length=40)
#     mobile_no = models.CharField(max_length=12)
#     gender = models.CharField(max_length=2)

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name
class Cart(models.Model):
    prod = models.ForeignKey(Product,on_delete=models.CASCADE)
    
    
