
class RightAtk:
    name = "right attack"

    def __init__(self, parent, gameMain):
        self.parent = parent
        self.gameMain = gameMain
    
    def ready(self):
        pass

    def action(self):
        players = self.gameMain.getPlayers()
        for player in players:
            if(player != self.parent and not "def right" in player.states):
                damages = 25
                self.parent.gainEnergy(2)
                player.takeDamages(damages)
                self.gameMain.results\
                    .append(f'{self.parent.name} right attack {player.name} for {damages}')
            elif(player != self.parent and "def right" in player.states):
                self.gameMain.results\
                    .append(f'{player.name} has block {self.parent.name} success')