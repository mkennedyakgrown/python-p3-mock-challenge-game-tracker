#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    game = Game("Game 1")
    player = Player("Johnny 1")
    result = Result(player, game, 1200)
    result = Result(player, game, 300)
    result = Result(player, game, 2000)

    print("Game result:")
    print(game.results())

    for result in Result.all:
        print(result.game)

    for game in Game.all:
        print(game.title)


    # ipdb.set_trace()
