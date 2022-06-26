from django.urls import path
from . import views
urlpatterns = [
    path('giris-yap/',views.login_user,name="giris_yap"),
    path('kayit-ol/',views.register,name="kayit_ol"),
    path('cikis-yap/',views.logout_user,name="cikis_yap"),
]
