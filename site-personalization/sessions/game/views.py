from django.shortcuts import render
from .models import Game, Player, PlayerGameInfo


def get_player_and_game(request, session_player_id, session_game_id):
    """Get player from db, if player ID in session
    If player ID not in session, creates new Player
    Return player instance, game_id, connected with player"""
    player_id, game_id = session_player_id, session_game_id
    game = None
    is_host = None
    if not player_id:
        player = Player()
        player.save()
    else:
        player = Player.objects.prefetch_related('game_id').get(id=int(player_id))
        game = player.game_id.first()
        if game:
            game_id = game.id
    if not game_id or player.game_id.first().is_finished:
        not_finised_game = Game.objects.filter(is_finished=False).first()
        if not_finised_game:
            game = not_finised_game
        else:
            number = request.GET.get('number')
            if number:
                number = int(number)
                game = Game(number=number, host=player)
                game.save()
        if game:
            player_game_info = PlayerGameInfo(player=player, game=game)
            player_game_info.save()
    else:
        game = Game.objects.get(id=int(game_id))
    if game:
        is_host = player == game.host
    return player, game, is_host


def show_home(request):
    player_id = request.session.get('player_id')
    game_id = request.session.get('game_id')
    player, game, is_host = get_player_and_game(request, player_id, game_id)
    hint = None
    is_finished = None
    game_number = None
    request.session['player_id'] = player.id
    if game:
        request.session['game_id'] = game.id
    if (not is_host) and game:
        guess = request.GET.get('guess')
        guess = int(guess) if guess else None
        if guess:
            if guess == game.number:
                game.is_finished = True
                game.save()
                game_number = guess
                is_finished = True
                game = None
            elif guess > game.number:
                hint = 'Число меньше'
            else:
                hint = 'Число больше'
    if game:
        is_finished = game.is_finished
    context = {'game': game,
               'player': player,
               'is_host': is_host,
               'is_finished': is_finished,
               'hint': hint,
               'game_number': game_number}
    return render(
        request,
        'home.html',
        context=context,
    )
