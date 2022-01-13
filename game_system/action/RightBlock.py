

from game_system.states.DefRight import DefRight

class RightBlock:
    name = "right block"

    def __init__(self, parent, gameMain):
        self.parent = parent
        self.gameMain = gameMain

    def ready(self):
        self.parent.addState(DefRight(self.parent, self.gameMain))
        self.gameMain.results\
                    .append(f'{self.parent.name} has defense right')

    def action(self):
        pass