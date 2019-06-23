from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleBadge


class ArticleBadgeInlineForemset(BaseInlineFormSet):
    def clean(self):
        is_main_count = 0
        for form in self.forms:
            data = form.cleaned_data
            if data.get('is_main'):
                is_main_count += 1
            if is_main_count > 1:
                raise ValidationError('Может быть только одна главная тема')


class TagInline(admin.TabularInline):
    model = ArticleBadge
    formset = ArticleBadgeInlineForemset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ['badges']


admin.site.register(Scope)
