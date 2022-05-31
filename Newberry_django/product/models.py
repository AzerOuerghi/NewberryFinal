from io import BytesIO
from unicodedata import category
from PIL import Image

from django.core.files import File
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.id}/'

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    
    description = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
        
    def get_category(self):
        return self.category.name
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.id}/{self.id}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
 

    
    
    