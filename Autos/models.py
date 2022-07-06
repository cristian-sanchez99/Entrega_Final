from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# Create your models here.
class Autos(models.Model):
    name = models.CharField(max_length= 30)
    description = models.CharField(max_length= 150,blank = True, null = True)
    price = models.FloatField()
    SKU = models.CharField(max_length= 30, unique=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to = "autos", null = True, blank = True)
    
    class Meta:
        verbose_name = "Auto"
        verbose_name_plural = "Autos"

