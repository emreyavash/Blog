from django.contrib import admin
from .models import Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fileds=("slug",)
    list_display=("CategoryName",)
admin.site.register(Category,CategoryAdmin);