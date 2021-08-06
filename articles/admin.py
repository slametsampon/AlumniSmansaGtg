from django.contrib import admin
from .models import Article, ArticleComment


# Minimal registration of Models.
admin.site.register(ArticleComment)

class ArticleCommentsInline(admin.TabularInline):
    """
    Used to show 'existing' blog comments inline below associated blogs
    """
    model = ArticleComment
    max_num=0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Administration object for Article models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields), grouping the date fields horizontally
     - adds inline addition of blog comments in blog view (inlines)
    """
    list_display = ('title', 'author', 'post_date')
    inlines = [ArticleCommentsInline]
