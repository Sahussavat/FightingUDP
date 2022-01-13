

class DefRight:

    cooldown = 1
    name = "def right"

    def __init__(self, parent, gameMain):
        self.parent = parent
        self.gameMain = gameMain

    def action(self):
        pass

    def reset(self):
        pass

    def update(self):
        self.cooldown -= 1
        if self.cooldown <= 0: 
            self.reset()
            del self.parent.states[self.name]
            self.gameMain.results\
            .append(f'{self.name} is out')