from django.contrib import admin
from .models import Post

admin.site.site_header = "Blog Administration"
admin.site.site_title = "Blog Admin Portal"
admin.site.index_title = "Welcome to Blog Admin"

admin.site.register(Post)
