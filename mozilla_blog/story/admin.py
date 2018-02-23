from django.contrib import admin
from .models import Comments, BlogPost, Blogger

admin.site.register(Blogger)
admin.site.register(BlogPost)
admin.site.register(Comments)