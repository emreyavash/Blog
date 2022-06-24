from .models import Blog,SliderBlog
from datetime import datetime
def editorblog(request):
    blogs = Blog.objects.filter(blog_status = True)[0:2]
    if blogs.exists():
        return {'blogs':blogs}
    else:
        return {'error':"Blog Yok"}
def sliderblog(request):
    sliders = SliderBlog.objects.filter(slider_status=True)
    return {'sliders':sliders}

def topPickMonth(request):
    monthBlogs = Blog.objects.filter(topPicksOfMonth=True)[0:3]
    return {'monthBlogs':monthBlogs}

def trendingblog(request):
    trendingblogs = Blog.objects.filter(trendingBlog = True)[0:2]
    return {'trendingblogs':trendingblogs}

