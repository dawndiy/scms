# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Tag, Article
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publish_time', 'status')  # ID, 标题， 作者， 时间， 状态
    list_filter = ('publish_time', )
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
