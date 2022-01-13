
class HeavyAtk:
    name = "heavy attack"

    def __init__(self, parent, gameMain):
        self.parent = parent
        self.gameMain = gameMain

    def ready(self):
        pass

    def action(self):
        players = self.gameMain.getPlayers()
        for player in players:
            if(player != self.parent and not "def block" in player.states \
                and self.parent.useEnergy(2)):
                damages = 50
                player.takeDamages(damages)
                self.gameMain.results\
                    .append(f'{self.parent.name} heavy attack {player.name} for {damages}')
            elif (player != self.parent and not self.parent.useEnergy(2)):
                self.gameMain.results\
                    .append(f'{self.parent.name} not have enough energy to use {self.name}')
            elif(player != self.parent and "def block" in player.states):
                self.gameMain.results\
                    .append(f'{player.name} has block {self.parent.name} success')