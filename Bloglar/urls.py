from django.urls import path
from . import views
urlpatterns = [
    path('<slug:slug>',views.BlogByCategoryListView.as_view(),name="bloglar"),
    path('Blog/<int:pk>',views.BlogDetailView.as_view(),name="blog_detail"),
    path('blog_comment/<int:id>',views.blogComment,name="blog_comment"),
    path('blog_search/',views.blogSearch,name="blog_search"),
]
