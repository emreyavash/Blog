from django.db import models
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    CategoryName=models.CharField(max_length=50)
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.CategoryName}"
    def save(self,*args, **kwargs):
        self.slug = slugify(self.CategoryName)
        super().save(*args, **kwargs)