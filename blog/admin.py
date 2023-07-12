from django.contrib import admin
from .models import Blog, SubContent, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_date']
    date_hierarchy = 'created_date'
    search_fields = ['title', 'tag', 'category']


admin.site.register(Blog, BlogAdmin)


class SubContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'sub_content']


admin.site.register(SubContent, SubContentAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'blog', 'top_level_comment_id', 'created_date' ]
    date_hierarchy = 'created_date'
    search_fields = ['author', 'blog']


admin.site.register(Comment, CommentAdmin)

