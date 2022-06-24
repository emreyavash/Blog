from . import views
from django.urls import path
urlpatterns = [
    path('Iletişim/',views.contactForm,name="iletisim")
]
