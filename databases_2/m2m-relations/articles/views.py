from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import Prefetch

from articles.models import Article, ArticleBadge


def articles_list(request):
    template = 'articles/news.html'
    context = {}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    articles = Article.objects.order_by(ordering).prefetch_related(
            Prefetch(
                     'scope_data',
                     queryset=ArticleBadge.objects.select_related('topic')
                    ))
    context['object_list'] = articles
    return render(request, template, context)
