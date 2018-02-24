from django.urls import path
from . import views

app_name = "story"
urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.index, name="index"),
    path("blog/<int:pk>", views.BlogPostDetailView.as_view(), name="blog-detail"),
    path("blog/blogs/", views.BlogPostListView.as_view(), name="blogs"),
    path("blog/blogger/<int:pk>", views.BloggerDetailView.as_view(), name="blogger-detail"),
    path("blog/bloggers/", views.BloggerListView.as_view(), name="bloggers"),
]
