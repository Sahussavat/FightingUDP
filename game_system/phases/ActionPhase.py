
from game_system.Server_Socket import Server_Socket

class ActionPhase:

    def __init__(self, gameMain):
        self.gameMain = gameMain

    def action(self):
        players = self.gameMain.getPlayers()
        Server_Socket.getInstance().action(next_mode="recv")
        for player in players: 
            Server_Socket.getInstance().action(f'{player.name} has HP: {player.hp}',"recv")
            Server_Socket.getInstance().action(\
                f'{player.name} has energy: {player.energy}',"recv")
        for player in players: player.show_action()
        for player in players: 
            if not player.isDead(): player.ready()
        for player in players: 
            if not player.isDead(): player.action()

    def next_phase(self):
        self.gameMain.currentPhase = self.gameMain.resultPhase
        