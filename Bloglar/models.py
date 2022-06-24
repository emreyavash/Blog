from django.db import models
from Writer.models import CustomUser
from Category.models import Category
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_description =models.TextField()
    blog_thumbnail = models.ImageField(upload_to="blogs")
    blog_image=models.ImageField(upload_to="blogs")
    writer = models.ForeignKey(CustomUser,related_name="blog_writer",null=False,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,related_name="blog_category",null=False,on_delete=models.CASCADE)
    blog_status = models.BooleanField(default=True)
    topPicksOfMonth = models.BooleanField(default=False)
    trendingBlog = models.BooleanField(default=False)
    create_blog_date = models.DateField(editable=False,auto_now_add=True)

class SliderBlog(models.Model):
    slider_title = models.CharField(max_length=100)
    slider_description = models.TextField()
    slider_image = models.ImageField(upload_to = 'slider')
    category = models.ForeignKey(Category,related_name="slider_category",null=False,on_delete=models.CASCADE)
    slider_status = models.BooleanField(default=True)
    create_slider_date = models.DateField(editable=False,auto_now_add=True)

class BlogComment(models.Model):
    blog= models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_comment')
    sender_name = models.CharField(max_length=50)
    sender_email = models.EmailField()
    comment = models.TextField()
    created_commnet_date = models.DateField(auto_now_add=True,editable=False)
    
