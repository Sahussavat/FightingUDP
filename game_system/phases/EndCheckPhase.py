
from game_system.players.Dummy import Dummy
from game_system.Server_Socket import Server_Socket

class EndCheckPhase:
    
    def __init__(self, gameMain):
        self.gameMain = gameMain

    def action(self):
        players = self.gameMain.getPlayers()
        isGameEnd = False
        for player in players:
            if players[0].isDead() and players[1].isDead():
                Server_Socket.getInstance().action("\nDraw\n","recv")
                break
            elif(player.isDead()): 
                isGameEnd = True
                if(isinstance(player, Dummy)):
                    Server_Socket.getInstance().action("\nYou Win\n","recv")
                else: Server_Socket.getInstance().action("\nYou Lose\n","recv")
                break
        self.gameMain.isGameEnd = isGameEnd

    def next_phase(self):
        if(self.gameMain.isGameEnd): 
            self.gameMain.currentPhase = self.gameMain.resetPlayer
        else: 
            self.gameMain.currentPhase = self.gameMain.updateStatePhase