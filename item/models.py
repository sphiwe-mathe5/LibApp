from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
        

    def __str__(self):
        return self.name

class Item(models.Model):
    Category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    hours = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    opened = models.BooleanField(default=False)
    opened_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    opened_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


