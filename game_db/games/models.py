from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name

class Price(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.price)

class Game(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    str_thumbnails = models.URLField()

    def __str__(self):
        return self.name

