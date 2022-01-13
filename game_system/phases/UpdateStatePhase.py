
class UpdateStatePhase:

    def __init__(self, gameMain):
        self.gameMain = gameMain
    
    def action(self):
        players = self.gameMain.getPlayers()
        for player in players:
            player.updateState()

    def next_phase(self):
        self.gameMain.currentPhase = self.gameMain.actionPhase