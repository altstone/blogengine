# coding=utf-8
from django.contrib import admin
from models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'get_title_shortened', 'get_excerpts', 'date_published']
    list_filter = ['date_published']
    search_fields = ['title', 'contents']
    fields = ['title', 'contents', 'date_published']
    readonly_fields = ['date_published']


admin.site.register(Post, PostAdmin)
