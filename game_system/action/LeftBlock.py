
from game_system.states.DefLeft import DefLeft


class LeftBlock:
    name = "left block"

    def __init__(self, parent, gameMain):
        self.parent = parent
        self.gameMain = gameMain

    def ready(self):
        self.parent.addState(DefLeft(self.parent, self.gameMain))
        self.gameMain.results\
                    .append(f'{self.parent.name} has defense left')

    def action(self):
        pass