from django.urls import path
from . import views
urlpatterns = [
    path('DashBoard/',views.admin_panel,name="admin_panel"),
    path('Bloglar/',views.blogs_list,name="blogs_list"),
    path('Blog-Düzenle/<int:id>',views.blog_edit,name="blog_edit"),
    path('Blog-Ekle/',views.blog_add,name="blog_add"),
    path('Blog-Sil/<int:id>',views.blog_delete,name="blog_delete"),
    path('Slider-Blog',views.slider_blog,name="slider_blog"),
    path('Slider-Blog-Ekle',views.slider_blog_add,name="slider_add"),
    path('Slider-Blog-Sil/<int:id>',views.slider_blog_delete,name="slider_blog_delete"),
    path('Slider-Blog-Düzenle/<int:id>',views.slider_blog_edit,name="slider_blog_edit"),
    path('Kategoriler/',views.category_list,name="category_list"),
    path('Kategori-Ekle/',views.category_add,name="category_add"),
    path('Kategori-Düzenle/<int:id>',views.category_edit,name="category_edit"),
    path('Kategori-Sil/<int:id>',views.category_delete,name="category_delete"),
    path('Kullanıcılar/',views.user_list,name="user_list"),
    path('Kullanıcı-Düzenle/<int:id>',views.user_edit,name="user_edit"),
    path('Kullanıcı-Sil/<int:id>',views.user_delete,name="user_delete"),
    path('Kullanıcı-Ekle/',views.user_add,name="user_add"),
    path('İletişim/',views.contact_list,name="contact_list"),
    path('İletişim/<int:id>',views.contact_delete,name="contact_delete"),
    path('İletişim/Mesaj/<int:id>',views.contact,name="contact"),


]
