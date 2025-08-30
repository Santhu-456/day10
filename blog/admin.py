from django.contrib import admin
from .models import Blog, Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    search_fields = ('title', 'content', 'author__username')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'get_user', 'email', 'date')
    def get_user(self, obj):
        return obj.user.username
    get_user.short_description = 'User'
    search_fields = ('post__title', 'user__username', 'content')
