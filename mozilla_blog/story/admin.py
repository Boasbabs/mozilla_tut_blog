from django.contrib import admin
from .models import Comment, BlogPost, Blogger


# Associated records to show in the admin
class BlogInline(admin.TabularInline):
    model = BlogPost


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name",)
    inlines = [BlogInline]


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "blogger", "post_date",)
    fields = [("title", "blogger"), "description", "post_date"]
    list_filter = ("post_date",)
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "blog", "post_time",)
    list_filter = ("author", "post_time",)


