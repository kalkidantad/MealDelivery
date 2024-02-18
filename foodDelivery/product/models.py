from django.db import models

# Create your models here.

#company info table 
#product info table 
class CompanyInformation(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    food_category = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.food_category

class Product(models.Model):
    dish_name = models.CharField(max_length=100)
    ingredients = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    #fields
    image = models.ImageField(null= True)
    # image = models.ImageField(upload_to='product_images/', null=True)

    price = models.FloatField(null=  True) 
    # restaurant = models.CharField(max_length = 100, null=True)
    
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    updated_at = models.DateTimeField(auto_now=True, null= True)

     

    def __str__(self) -> str:
        return self.dish_name
 
