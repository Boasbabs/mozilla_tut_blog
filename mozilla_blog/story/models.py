from django.db import models
from django.utils import timezone
from django.shortcuts import reverse


class Blogger(models.Model):
    """
    This model is for those who write the blogs
    """
    first_name = models.CharField(max_length=15, help_text="Enter your first name")
    last_name = models.CharField(max_length=15, help_text="Enter your last name")
    bio = models.TextField(max_length=500, help_text="Your brief history")

    class Meta:
        ordering = ["-first_name"]

    def get_absolute_url(self):
        return reverse("blogger-detail", args=[str(self.id)])

    def __str__(self):
        """
        String representation of the blogger object
        :return:
        """
        return "{0}, {1}".format(self.last_name, self.first_name)


class BlogPost(models.Model):
    """
    Blog post by the authors
    """
    title = models.CharField(max_length=225, help_text="Enter the title of your blog")
    blogger = models.ForeignKey("Blogger", on_delete=models.CASCADE)
    description = models.TextField(max_length=2000, help_text="Write your article")
    post_date = models.DateTimeField("date posted", default=timezone.now)

    class Meta:
        """To order the post by newest first"""
        ordering = ["-post_date"]

    def get_absolute_url(self):
        """Returns the url to access a particular instance of model"""
        return reverse("blog-detail", args=[str(self.id)])

    def __str__(self):
        """
        String representation of the blog post object
        :return:
        """
        return self.title


class Comments(models.Model):
    """
    This is model for comment a each specific blog post
    """
    author = models.ForeignKey("Blogger", on_delete=models.CASCADE)
    comment = models.TextField(max_length=500, help_text="Enter your comments")
    post_time = models.DateTimeField("time posted", default=timezone.now)
    blog = models.ForeignKey("BlogPost", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-post_time"]

    def __str__(self):
        """String representation of the comments object"""
        return self.comment

