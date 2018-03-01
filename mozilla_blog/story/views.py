from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from .models import Blogger, BlogPost, Comment


def index(request):
    return render(request, "story/index.html")


class BlogPostListView(generic.ListView):
    model = BlogPost
    # context_object_name = "my_blog_list"
    # queryset = BlogPost.objects.all()
    template_name = "story/blog_list.html"


class BlogPostDetailView(generic.DetailView):
    model = BlogPost
    context_object_name = "my_blog_detail"
    template_name = "story/blog_detail.html"


class BloggerListView(generic.ListView):
    model = Blogger
    template_name = "story/blogger_list.html"


class BloggerDetailView(generic.DetailView):
    model = Blogger
    template_name = "story/blogger_detail.html"

