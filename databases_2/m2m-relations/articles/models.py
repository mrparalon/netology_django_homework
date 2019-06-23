from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    scopes = models.ManyToManyField('Scope', through='ArticleBadge')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):
    topic = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статей'

    def __str__(self):
        return self.topic


class ArticleBadge(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='scope_data')
    topic = models.ForeignKey(Scope, on_delete=models.CASCADE,
                              related_name='scope_data')
    is_main = models.BooleanField()
