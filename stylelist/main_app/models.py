from django.db import models
from django.contrib.auth.models import User 
from datetime import date 
from django.urls import reverse 

# Tuples for Apparel Model will be here
TYPES = (
    ('T', 'Top'),
    ('B', 'Bottom'),
    ('S', 'Shoe')
)

# Create your models here.

# User model (will be a subclass of the already made django user model so i can add special features?)


#Apparel Model 
class Apparel(models.Model):
    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=40)
    color = models.CharField(max_length=30)
    size = models.CharField(max_length=40)
    img = models.ImageField(default='images/img-error.png')
    style = models.CharField(max_length=70, default='not specified')
    type = models.CharField(
        max_length=1,
        choices = TYPES, 
        default = TYPES[0][0]
    )

    def __str__(self):
        return f'{self.type} : {self.name}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'apparel_id': self.id })
    
     


# Outfit Model 
class Outfit(models.Model):
    name = models.CharField(max_length=40)
    date = models.DateField('Date Made')
    event = models.CharField(max_length=40)
    caption = models.CharField(max_length=50)

    apparels = models.ManyToManyField(Apparel)




