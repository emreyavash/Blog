from django.urls import path,re_path
from . import views
urlpatterns = [
    path('writer-dashboard/<int:id>',views.writerDashboard,name="writer_dashboard"),
    path('bloglarim/<int:id>',views.writer_blog,name="bloglarim"),
    path('blog-ekle/<int:id>',views.add_blog,name="add_blog"),
    path('blog-düzenle/<int:id>',views.edit_blog,name="edit_blog"),
    path('blog-sil/<int:id>',views.delete_blog,name="delete_blog"),
    path('ayarlar/<int:id>',views.settings_user,name="settings_user"),
    path('sifre-degistir/<int:id>',views.reset_password,name="reset_password"),
]
