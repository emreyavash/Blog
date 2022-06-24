from multiprocessing import context
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Contact
# Create your views here.

def contactForm(request):
    if request.method =="POST":
        name = request.POST["name"]
        subject = request.POST["subject"]
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact = Contact.objects.create(name=name,subject = subject,email=email,phone_number = phone,message = message)
        contact.save()
        messages.success(request,"Gönderim Başarılı")
        return redirect('iletisim')
    else:
        return render(request,'contact/contact.html')