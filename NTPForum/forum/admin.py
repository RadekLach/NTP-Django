from django.contrib import admin
from .models import Thread
from .models import Post

# Better way is to override admin template, but this is shorter
admin.site.site_header = "Administration"

class PostInline(admin.TabularInline):
    # Posts will be available in Threads
    model = Post

class ThreadAdmin(admin.ModelAdmin):
    model = Thread
    inlines = [PostInline]

admin.site.register(Thread, ThreadAdmin)
