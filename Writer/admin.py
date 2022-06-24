from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):

   
    list_display=("email","first_name","last_name","is_active","is_staff")
    search_fields = ("email","first_name",)
    def genderName(self,obj):
        html = ""
        if obj.gender == "1":
            html+="Male"
        else:
            html+="Female"

        return html
    fieldsets = [
        ("Kullancı Bilgileri", {'fields': ['first_name']}),   
        (None, {'fields': ['last_name']}),
        (None, {'fields': ['email']}),   
        (None, {'fields': ['password']}),   
        (None, {'fields': ['profil_image']}),   
        (None, {'fields': ['birthday']}),
        (None, {'fields': ['gender']}),   
        ("Yetki Bilgileri", {'fields': ['is_superuser']}),   
        (None, {'fields': ['is_active']}),
        (None, {'fields': ['is_staff']}),   
        ("Zaman Bilgileri", {'fields': ['date_joined']}),   
        
        (None, {'fields': ['last_login']}),   
    ]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name','last_name','password1', 'password2','profil_image','gender','birthday' ,'is_staff', 'is_active')}
        ),
    )
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)