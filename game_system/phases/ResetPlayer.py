
class ResetPlayer:

    def __init__(self, gameMain):
        self.gameMain = gameMain
    
    def action(self):
        players = self.gameMain.getInstance().getPlayers()
        for player in players:
            player.reset()

    def next_phase(self):
        self.gameMain.getInstance().currentPhase = self.gameMain.getInstance().actionPhase