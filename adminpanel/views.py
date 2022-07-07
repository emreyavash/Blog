from multiprocessing import context
from urllib import request
from django.shortcuts import redirect, render
from Writer.models import CustomUser
from Category.models import Category
from Bloglar.models import Blog,BlogComment,SliderBlog
from Contact.models import Contact
from django.db.models import Count
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def user_authenticated(user):
    try:
        id = user.id
        admin = CustomUser.objects.get(id = id)
        print(admin.is_superuser)
        if admin.is_superuser:
            return user.is_authenticated 
        else:
            return False
    except CustomUser.DoesNotExist:
        return False

@user_passes_test(user_authenticated,login_url='Home')
def admin_panel(request):
    
    users = CustomUser.objects.all()
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    blogcountBycategory = []
    for ct in categories:
        blogsbycategory = Blog.objects.filter(category=ct.id).count()
        blogcountBycategory.append(blogsbycategory)
    context={
        'users':users,
        'blogs':blogs,
        'categories':categories,
        'denemblogcountBycategorye':blogcountBycategory
    }
    return render(request,'adminpanel/dashboard.html',context)
    

@user_passes_test(user_authenticated,login_url='Home')
def blogs_list(request):
    
    blogs = Blog.objects.all()

    context={
        'blogs':blogs
    }
    return render(request,'adminpanel/blogs_list.html',context)

@user_passes_test(user_authenticated,login_url='Home')
def blog_edit(request,id):
    blog = Blog.objects.get(id = id)
    categories = Category.objects.all()
    if request.method == "POST":
        blog.writer = blog.writer
        blog.blog_title = request.POST['blog_title']
        blog.blog_description = request.POST['blog_description']
        if request.FILES.get('blog_thumbnail') is None:
            blog.blog_thumbnail = request.POST['hidden_thumbnail']
        else:
            blog.blog_thumbnail = request.FILES['blog_thumbnail']
        if request.FILES.get('blog_image') is None:
            blog.image = request.POST['hidden_image']
        else:
            blog.image = request.FILES['blog_image']
        category = request.POST['category']
        blog.category = Category.objects.get(CategoryName = category)
        blog.topPicksOfMonth = request.POST.get('topPicksOfMonth',False)
        blog.trendingBlog = request.POST.get('trendingBlog',False)
        blog.blog_status = request.POST['status']
        blog.save()
        return redirect("blog_edit",blog.id)
    context={
        'blog':blog,
        'categories':categories,
    }
    return render(request,'adminpanel/blog_edit.html',context)

@user_passes_test(user_authenticated,login_url='Home')
def blog_add(request):
    id = request.user.id
    writer_admin = CustomUser.objects.get(Q(id = id),Q(is_superuser=True))
    if request.method == "POST":
        blog_title = request.POST['blog_title']
        blog_description = request.POST['blog_description']
        blog_thumbnail = request.FILES['blog_thumbnail']
        blog_image = request.FILES['blog_image']
        category = Category.objects.get(CategoryName = request.POST['category'])
        topPicksOfMonth = request.POST.get('topPicksOfMonth',False)
        trendingBlog = request.POST.get('trendingBlog',False)
        blog_status = request.POST['status']
        admin_blog = Blog.objects.create(blog_title=blog_title,blog_description=blog_description,blog_thumbnail=blog_thumbnail,blog_image=blog_image,category_id=category.id,topPicksOfMonth=topPicksOfMonth,trendingBlog=trendingBlog,blog_status=blog_status,writer_id= id)
        admin_blog.save()
        return redirect("blogs_list")

    context={
        'writer_admin':writer_admin
    }
    return render(request,'adminpanel/blog_add.html',context)

@user_passes_test(user_authenticated,login_url='Home')
def blog_delete(request,id):
    blog = Blog.objects.get(id = id)
    blog.blog_status = False
    blog.save()
    return redirect("blogs_list")

        
@user_passes_test(user_authenticated,login_url='Home')
def slider_blog(request):
    slider_blogs = SliderBlog.objects.all()
    context = {
        'slider_blogs':slider_blogs
    }
    return render(request,'adminpanel/slider_blog.html',context)

@user_passes_test(user_authenticated,login_url='Home')
def slider_blog_edit(request,id):
    slider_blog = SliderBlog.objects.get(id = id)
    categories = Category.objects.all()
    if request.method == "POST":
        slider_blog.slider_title = request.POST['slider_title']
        slider_blog.slider_description = request.POST['slider_description']
        if request.FILES.get('slider_image') is None:
            slider_blog.slider_image = request.POST['hidden_image']
        else:
            slider_blog.slider_image = request.FILES['slider_image']
        slider_blog.category = Category.objects.get(CategoryName = request.POST['category'])
        slider_blog.slider_status = request.POST['status']
        slider_blog.save()
        return redirect('slider_blog_edit',slider_blog.id)
    context={
        'slider_blog':slider_blog,
        'categories':categories
    }
    return render(request,'adminpanel/slider_edit.html',context)

@user_passes_test(user_authenticated,login_url='Home')
def slider_blog_add(request):
    categories = Category.objects.all()
    if request.method == "POST":
        slider_title = request.POST['slider_title']
        slider_description = request.POST['slider_description']
        slider_image = request.FILES['slider_image']
        category = Category.objects.get(CategoryName = request.POST['category'])
        slider_status = request.POST['status']
        slider_blog = SliderBlog.objects.create(slider_title = slider_title,slider_description=slider_description,slider_image= slider_image,category = category,slider_status = slider_status)
        slider_blog.save()
        return redirect('slider_blog')
    context={
        "categories":categories
    }
    return render(request,'adminpanel/slider_add.html',context)
    
        

@user_passes_test(user_authenticated,login_url='Home')
def slider_blog_delete(request,id):
    slider_blog = SliderBlog.objects.get(id = id)
    slider_blog.slider_status = False
    slider_blog.save()
    return redirect("slider_blog")

@user_passes_test(user_authenticated,login_url='Home')
def category_list(request):
    categories = Category.objects.all()
    context={
        'categories':categories
    }
    return render(request,'adminpanel/category_list.html',context)

@user_passes_test(user_authenticated,login_url='Home')
def category_add(request):
    if request.method == "POST":
        category_name = request.POST['category_name']
        category_status = request.POST['status']
        category = Category.objects.create(CategoryName = category_name,status = category_status)
        category.save()
        return redirect("category_list")
    return render(request,"adminpanel/category_add.html")

@user_passes_test(user_authenticated,login_url='Home')
def category_edit(request,id):
    category = Category.objects.get(id = id)
    if request.method == "POST":
        category.CategoryName = request.POST['category_name']
        category.status = request.POST['status']
        category.save()
        return redirect('category_list')
    context={
        'category':category
    }
    return render(request,'adminpanel/category_edit.html',context)

@user_passes_test(user_authenticated,login_url='Home')
def category_delete(request,id):
    category = Category.objects.get(id = id)
    category.status = False
    category.save()
    return redirect("category_list")

@user_passes_test(user_authenticated,login_url='Home')
def user_list(request):
    users = CustomUser.objects.all()
    context={
        'users':users,
    }
    return render(request,'adminpanel/users_list.html',context)

@user_passes_test(user_authenticated,login_url='Home')
def user_edit(request,id):
    user = CustomUser.objects.get(id = id)
    if request.method == 'POST':
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.gender = request.POST['gender']
        user.is_active = request.POST['is_active']
        if request.FILES.get('profil_image') is None:
            user.profil_image = request.POST['hidden_image']
        else:
            user.profil_image = request.FILES['profil_image']
        user.save()
        return redirect('user_list')
    context={
        'user':user
    }
    return render(request,'adminpanel/user_edit.html',context)

@user_passes_test(user_authenticated,login_url='Home')
def user_delete(request,id):
    user = CustomUser.objects.get(id = id)
    user.is_active = False
    user.save()
    return redirect("user_list")

@user_passes_test(user_authenticated,login_url='Home')
def user_add(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        profil_image = request.FILES['profil_image']
        gender = request.POST['gender']
        is_active = request.POST['is_active']
        user = CustomUser.objects.create(first_name=first_name,last_name = last_name,email = email,profil_image = profil_image,gender =gender,is_active = is_active)
        user.save()
        return redirect('user_list')

    else:
        return render(request,'adminpanel/user_add.html')

@user_passes_test(user_authenticated,login_url='Home')
def contact_list(request):
    contacts= Contact.objects.all()
    context={
        'contacts':contacts
    }
    return render(request,'adminpanel/contact_list.html',context)

@user_passes_test(user_authenticated,login_url='Home')
def contact(request,id):
    mesaj =  Contact.objects.get(id = id)
    context ={
        'mesaj':mesaj
    }
    return render(request,'adminpanel/contact.html',context)
@user_passes_test(user_authenticated,login_url='Home')
def contact_delete(request,id):
    message = Contact.objects.get(id = id)
    message.delete()
    return redirect("contact_list")