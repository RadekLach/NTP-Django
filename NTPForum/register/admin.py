from django.contrib import admin
from django.contrib.auth.models import User
from forum.models import Thread
from forum.admin import PostInline

class ThreadInline(admin.TabularInline):
    model = Thread

class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = [ThreadInline, PostInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
