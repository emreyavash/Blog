from django.contrib import admin
from .models import Blog,SliderBlog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display= ('blog_title','writer')
class SliderBlogAdmin(admin.ModelAdmin):
    list_display= ('slider_title',)

admin.site.register(Blog,BlogAdmin)
admin.site.register(SliderBlog,SliderBlogAdmin)