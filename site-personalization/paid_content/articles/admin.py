from django.contrib import admin
from articles.models import Article, Profile


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_paid']
    pass


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_premium']
    pass

admin.site.register(Article, ArticleAdmin)
admin.site.register(Profile, ProfileAdmin)