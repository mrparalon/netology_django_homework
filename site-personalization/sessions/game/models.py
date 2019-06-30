from django.db import models


class Player(models.Model):
    game_id = models.ManyToManyField('Game', through='PlayerGameInfo')


class Game(models.Model):
    number = models.IntegerField()
    is_finished = models.BooleanField(default=False)
    host = models.ForeignKey('Player', on_delete=models.CASCADE)


class PlayerGameInfo(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)