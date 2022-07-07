from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from Category.models import Category
from .models import CustomUser
from Bloglar.models import Blog,BlogComment
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from channels.layers import get_channel_layer
# Create your views here.

def user_authenticated(user):
    try:
        return user.is_authenticated 
    except CustomUser.DoesNotExist:
        return False

@user_passes_test(user_authenticated,login_url='Home')
def writerDashboard(request,id):
    writer = CustomUser.objects.get(id = id)
    if request.user.id != writer.id :
        return redirect('Home')
    writer_blogs = Blog.objects.filter(Q(writer = id),Q(blog_status = True))[0:3]
    blog_comments = BlogComment.objects.filter(writer = id)[0:6]
    if blog_comments.exists() and writer_blogs.exists():
        context={
            'writer':writer,
            'writer_blogs':writer_blogs,
            'blog_comments':blog_comments,
            'room_name':"broadcast"
        }
    elif blog_comments.exists():
        context={
            'writer_error':"Şu an da paylaştığınız bloğunuz yok.",
            'writer':writer,
            'blog_comments':blog_comments,
            'room_name':"broadcast"

            
        }
    elif writer_blogs.exists():
        context={
            'comments_error':"Şu an da yorum yapılan bloğunuz yok.",
            'writer':writer,
            'writer_blogs':writer_blogs,
            'room_name':"broadcast"
            
        }
    else:
        context={
            'comments_error':"Şu an da yorum yapılan bloğunuz yok.",
            'writer':writer,
            'writer_error':"Şu an da paylaştığınız bloğunuz yok.",
            'room_name':"broadcast"
            
        }
    return render(request,'writer/dashboard.html',context)

@user_passes_test(user_authenticated,login_url='Home')
def writer_blog(request,id):
    writer_blogs = Blog.objects.filter(Q(writer = id),Q(blog_status = True))
    if request.user.id != id:
        return redirect('Home')
    print(request.user.id)
    print(id)
    if writer_blogs.exists():
        context={
            'writer_blogs':writer_blogs
        }
    else:
        context={
            'blogs_error':"Henüz blog yazısı paylaşmadınız."
        }
    return render(request,'writer/writer_blog.html',context)
@user_passes_test(user_authenticated,login_url='Home')
def add_blog(request,id):
    if request.user.id !=id :
        return redirect('Home')
    writer = CustomUser.objects.get(id = id)
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        thumbnail = request.FILES['thumbnail']
        image = request.FILES['image']
        category = request.POST['category']
        category = Category.objects.get(id=category)
        blog = Blog.objects.create(blog_title= title,blog_description= description,blog_thumbnail = thumbnail,blog_image=image,blog_status=True,writer = writer,category= category)
        blog.save()
        return redirect('bloglarim',writer.id)
    return render(request,'writer/add_blog.html')

@user_passes_test(user_authenticated,login_url='Home')
def edit_blog(request,id):
    blog = Blog.objects.get(id = id)

    if request.user.id !=blog.writer.id :
        return redirect('Home')
    if request.method == 'POST':
        blog.blog_title = request.POST['title']
        blog.blog_description = request.POST['description']
        if request.FILES.get('thumbnail') is None:
            blog.blog_thumbnail = request.POST['hidden_thumbnail']

        else:
            blog.blog_thumbnail = request.FILES['thumbnail']
        if request.FILES.get('image') is None:
            blog.blog_image = request.POST['hidden_image']

        else:
            blog.blog_image = request.FILES['image']
        category = request.POST['category']
        blog.category = Category.objects.get(id=category)
        # blog = blog.update(blog_title= title,blog_description= description,blog_thumbnail = thumbnail,blog_image=image,blog_status=True,category= category)
        blog.save()
        return redirect('bloglarim',blog.writer.id)
    context={
        'blog':blog
    }
    return render(request,'writer/edit_blog.html',context)

@user_passes_test(user_authenticated,login_url='Home')
def delete_blog(request,id):
    blog = Blog.objects.get(id = id)
    if request.user.id !=blog.writer.id :
        return redirect('Home')
    blog.delete()
    return redirect('bloglarim',blog.writer.id)
    
@user_passes_test(user_authenticated,login_url='Home')
def settings_user(request,id):
    writer = CustomUser.objects.get(id = id)
    if request.user.id !=writer.id :
        return redirect('Home')
    if request.method == "POST":
        writer.first_name = request.POST['first_name']
        writer.last_name = request.POST['last_name']
        if request.FILES.get('profil_image') is None:
            writer.profil_image = request.POST['hidden_profil_image']
        else:
            writer.profil_image = request.FILES['profil_image']

        writer.birthday = request.POST['birthday']
        writer.gender = request.POST['gender']
        writer.save()
        print(writer.first_name)
        return redirect('writer_dashboard',writer.id)
    else:
        context = {
            'writer':writer
        }
        return render(request,"writer/settings.html",context)

@user_passes_test(user_authenticated,login_url='Home')
def reset_password(request,id):
    writer = CustomUser.objects.get(id = id)
    if request.user.id !=writer.id :
        return redirect('Home')
    if request.method == "POST":
        old_password = request.POST['old_password']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.error(request,'Şifreniz Eşleşmiyor.')
            return redirect('settings_user',writer.id)
        
        checked_password = check_password(old_password,writer.password)
        if checked_password:
            writer.set_password(password1)
            writer.save()
            messages.success(request,'Şifreniz Değiştirildi.')
            return redirect('settings_user',writer.id)
        else:
            messages.error(request,'Eski Şifreniz Eşleşmiyor.')
            return redirect('settings_user',writer.id)

