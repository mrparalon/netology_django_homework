from django.db import models


class Car(models.Model):
    brand = models.CharField('Бренд', max_length=50)
    model = models.CharField('Модель', max_length=50)

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        return Review.objects.filter(car=self).count()

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE,
                            verbose_name='Автомобиль')
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст')

    def __str__(self):
        return str(self.car) + ' ' + self.title
    
    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'

