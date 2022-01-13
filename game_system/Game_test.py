
from GameMain import GameMain
from players.Player import Player
from players.Dummy import Dummy

GameMain.getInstance().connectPlayer(Player("Jack", None))
GameMain.getInstance().connectPlayer(Dummy())
GameMain.getInstance().start_game()