from django.shortcuts import render
from articles.models import Article, Profile


def show_articles(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(
        request,
        'articles.html',
        context=context,
    )


def show_article(request, id):
    article = Article.objects.get(id=id)
    user = None
    if request.user.is_authenticated:
        user = Profile.objects.get(user=request.user.id)
    context = {'article': article,
               'user': user}
    return render(
        request,
        'article.html',
        context=context
    )


def pay(request):
    user = Profile.objects.get(user=request.user.id)
    print(request.GET.get('make_premium'))
    print(request.GET.get(type('make_premium')))
    if request.GET.get('make_premium') == '1':
        user.is_premium = True
        user.save()
    context = {'user': user}
    return render(
        request,
        'pay.html',
        context=context
    )