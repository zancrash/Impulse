from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Category database model: create table 'Category' with id field (auto created) and name field
class Category(models.Model):
  name = models.CharField(max_length=255)

  class Meta:
    ordering = ('name',)
    verbose_name_plural = "Categories"

  def __str__(self):
    return self.name # show actual Category name, rather than "Category Object"
  
class Item(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)
  category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
  price = models.FloatField()
  image = models.ImageField(upload_to='items_images', blank=True, null=True)
  is_sold = models.BooleanField(default=False)
  created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
