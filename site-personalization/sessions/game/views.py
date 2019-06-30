from django.shortcuts import render
from .models import Game, Player, PlayerGameInfo
from random import randint


def get_player_and_game(session_player_id, session_game_id):
    """Get player from db, if player ID in session
    If player ID not in session, creates new Player
    Return player instance, game_id, connected with player"""
    player_id, game_id = session_player_id, session_game_id
    if not player_id:
        player = Player()
        player.save()
    else:
        player = Player.objects.prefetch_related('game_id').get(id=int(player_id))
        game = player.game_id.first()
        game_id = game.id
    if not game_id or player.game_id.first().is_finished:
        not_finised_game = Game.objects.filter(is_finished=False).first()
        if not_finised_game:
            game = not_finised_game
        else:
            game = Game(number=randint(1, 10), host=player)
            game.save()
        player_game_info = PlayerGameInfo(player=player, game=game)
        player_game_info.save()
    else:
        game = Game.objects.get(id=int(game_id))
    is_host = player == game.host
    return player, game, is_host


def show_home(request):
    player_id = request.session.get('player_id')
    game_id = request.session.get('game_id')
    player, game, is_host = get_player_and_game(player_id, game_id)
    hint = None
    request.session['player_id'] = player.id
    request.session['game_id'] = game.id
    if not is_host:
        guess = request.GET.get('guess')
        guess = int(guess) if guess else None
        if guess:
            if guess == game.number:
                game.is_finished = True
                game.save()
            elif guess > game.number:
                hint = 'Число меньше'
            else:
                hint = 'Число больше'
    context = {'game': game,
               'player': player,
               'is_host': is_host,
               'is_finished': game.is_finished,
               'hint': hint}
    return render(
        request,
        'home.html',
        context=context,
    )
