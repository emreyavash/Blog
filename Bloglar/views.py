from urllib import request
from django.shortcuts import redirect, render
from django import template
from django.core.exceptions import ObjectDoesNotExist
from .models import Blog,BlogComment
from Category.models import Category
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from Writer.models import CustomUser
# Create your views here.

class BlogByCategoryListView(ListView):
    model=Blog
    template_name="bloglar/BlogsByCategory.html"
    context_object_name="blogs"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug = self.kwargs['slug'])
        return context
    def get_queryset(self,*args, **kwargs):
        categoryid = Category.objects.get(slug = self.kwargs['slug'])
        return Blog.objects.filter(Q(category = categoryid),Q(blog_status = True) )

class BlogDetailView(DetailView):
    model=Blog
    template_name="bloglar/blogdetail.html"
    context_object_name="blog"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog= Blog.objects.get(id=self.kwargs['pk'])
       
        context['resentPosts'] = Blog.objects.order_by('-create_blog_date')[:3]
        context['likeBlogs'] = Blog.objects.exclude(id = self.kwargs['pk']).filter(category = blog.category)[:3]
      
        blogComment=BlogComment.objects.filter(blog= blog.id)
        if blogComment.exists():
            commentCount = blogComment.count()
           

            context['commentBlogs'] = blogComment
            context['commentCount'] = commentCount
                
        else:
            context['error']="Henüz yorum yapılmadı..!"
        return context
    def get_queryset(self):
        return Blog.objects.filter(id=self.kwargs['pk'])

def blogComment(request,id):
    blog_id = Blog.objects.get(id = id)
    if request.method =="POST":
        name= request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']

        commentBlog = BlogComment.objects.create(sender_name = name,sender_email = email,comment = comment,blog_id=blog_id.id,writer=blog_id.writer)
        commentBlog.save()
        return redirect("blog_detail",id)

def blogSearch(request):
    if request.method == "GET":
        search = request.GET['search']

        search_blog = Blog.objects.filter(blog_title__icontains=search)
        context={
            'blogs':search_blog,
            "search":search
        }
        return render(request,'bloglar/BlogsBySearch.html',context)
    