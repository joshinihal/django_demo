from django.db import models
 
# Create your models here.
 
 
class Category(models.Model):
    topic = models.CharField(max_length=264, unique=True)
 
    def __str__(self):
        return self.topic
 
 
class Brand(models.Model):
    brand = models.CharField(max_length=264, unique=True)
 
    def __str__(self):
        return self.brand
 
 
class Employee(models.Model):
    name = models.CharField(max_length=264, unique=True, null=True)
 
    def __str__(self):
        return self.name
 
 
class Webpage(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)
 
    def __str__(self):
        return self.name
 
 
class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    date = models.DateField()
 
    def __str__(self):
        return str(self.date)