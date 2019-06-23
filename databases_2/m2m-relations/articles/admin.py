from django.contrib import admin

from .models import Article, Scope, ArticleBadge


class TagInline(admin.TabularInline):
    model = ArticleBadge
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ['badges']


admin.site.register(Scope)
