from django.contrib import admin
from .models import Article, Paragraph, MediaAttachment


class ParagraphInline(admin.TabularInline):
    model = Paragraph
    extra = 1
    ordering = ['order']


class MediaInline(admin.TabularInline):
    model = MediaAttachment
    extra = 1
    ordering = ['order']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_published')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'summary', 'author')
    inlines = [ParagraphInline, MediaInline]
    prepopulated_fields = {}
