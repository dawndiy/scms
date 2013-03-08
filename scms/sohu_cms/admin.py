from django.contrib import admin
from models import Author, Category, Article

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', )
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publish_time')
    list_filter = ('publish_time', )
    
admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
