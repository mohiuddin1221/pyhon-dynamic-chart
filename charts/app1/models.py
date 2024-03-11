from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length =20, unique = True)
    
    def __str__(self) :
        return self.name
    
class Year(models.Model):
    name = models.PositiveIntegerField(unique = True)
    
    def __str__(self):
        return str(self.name)
    
class SuicideCase(models.Model):
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    year = models.ForeignKey(Year, on_delete = models.CASCADE)
    case = models.PositiveIntegerField()
    
