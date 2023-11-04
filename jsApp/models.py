from django.db import models
 
class Stuednts(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
