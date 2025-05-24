from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string


# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True,) 
    
    def __str__(self):
        return self.name
    
class Note(models.Model):
    
    
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True,)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate Intial SLug:
            slug_base = slugify(self.title)
            slug = slug_base
            # Check if the slug is unique and modify it if neccessary
            if Note.objects.filter(slug=slug).exists():
                slug = f"{slug_base}--{get_random_string(5)}"
            self.slug = slug
        super(Note, self).save(*args, **kwargs)
        
