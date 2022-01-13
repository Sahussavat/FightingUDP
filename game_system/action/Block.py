
from game_system.states.BuffDef import BuffDef


class Block:
    name = "heavy block"

    def __init__(self, parent, gameMain):
        self.parent = parent
        self.gameMain = gameMain

    def ready(self):
        self.parent.addState(BuffDef(self.parent, self.gameMain))
        self.gameMain.results\
                    .append(f'{self.parent.name} has defense block')

    def action(self):
        pass