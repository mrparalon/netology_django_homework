from django.shortcuts import render
from django.db.models import Prefetch

from articles.models import Article, ArticleBadge


def articles_list(request):
    template = 'articles/news.html'
    context = {}
    ordering = '-published_at'
    articles = Article.objects.order_by(ordering).prefetch_related(
            Prefetch(
                'scope_data',
                queryset=ArticleBadge.objects.select_related('topic').
                                            order_by('-is_main', '-topic')
                    ))
    context['object_list'] = articles
    return render(request, template, context)
