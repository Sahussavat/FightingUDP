
class LeftAtk:
    name = "left attack"

    def __init__(self, parent, gameMain):
        self.parent = parent
        self.gameMain = gameMain

    def ready(self):
        pass

    def action(self):
        players = self.gameMain.getPlayers()
        for player in players:
            if(player != self.parent and not "def left" in player.states):
                damages = 25
                self.parent.gainEnergy(2)
                player.takeDamages(damages)
                self.gameMain.results\
                    .append(f'{self.parent.name} left attack {player.name} for {damages}')
            elif(player != self.parent and "def left" in player.states):
                self.gameMain.results\
                    .append(f'{player.name} has block {self.parent.name} success')