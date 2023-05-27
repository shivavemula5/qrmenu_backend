from django.db import models
from django.conf import settings

class Place(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    number_of_tables = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.name}'

class Category(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE,related_name='category')
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.place.name} / {self.name}'

class MenuItem(models.Model):
    place = models.ForeignKey(Place,on_delete=models.CASCADE,related_name='menuitem')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='menuitem')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.place.name} / {self.category.name} / {self.name}'