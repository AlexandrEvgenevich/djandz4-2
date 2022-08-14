from django.contrib import admin
from .models import Article, Scopes, Topic


class ScopesInline(admin.TabularInline):
    model = Scopes


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    list_filter = ['published_at']
    inlines = [ScopesInline]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name']
