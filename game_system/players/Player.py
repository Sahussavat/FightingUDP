
from game_system.action.RightAtk import RightAtk
from game_system.action.LeftAtk import LeftAtk
from game_system.action.HeavyAtk import HeavyAtk
from game_system.action.LeftBlock import LeftBlock
from game_system.action.RightBlock import RightBlock
from game_system.action.Block import Block
from game_system.Server_Socket import Server_Socket

class Player:

    MAX_HP = 100
    hp = MAX_HP

    defense = 0
    MAX_ENERGY = 3
    energy = 0

    currentAction = None

    states = {}
    
    #====================================================
    def __init__(self, name, gameMain):
        self.name = name
        self.gameMain = gameMain
        self.actions = [
                RightAtk(self, gameMain),
                LeftAtk(self, gameMain),
                HeavyAtk(self, gameMain),
                LeftBlock(self, gameMain),
                RightBlock(self, gameMain),
                Block(self, gameMain)
            ]
    #====================================================
    def takeDamages(self, damages):
        self.hp = self.hp - (damages - self.defense)
        if self.hp < 0: self.hp = 0
        if self.isDead(): self.gameMain.results\
            .append(f'{self.name} is Dead')

    def useEnergy(self, energy):
        if self.energy - energy < 0: return False
        self.energy -= energy
        return True

    def gainEnergy(self, energy):
        self.energy += energy
        if(self.energy > self.MAX_ENERGY): self.energy = self.MAX_ENERGY
        
    def isDead(self):
        return self.hp <= 0
    #====================================================
    def show_action(self):
        i = 0
        for action in self.actions:
            i += 1
            Server_Socket.getInstance().action(f'{i} {action.name}',"recv")
        Server_Socket.getInstance().action(next_mode="send")
        num, conn, addr = Server_Socket.getInstance().action("Choose action: ", "recv")
        while not num.isnumeric():
            Server_Socket.getInstance().action(f'Please enter only 1-{len(self.actions)}',"send")
            num, conn, addr = Server_Socket.getInstance().action("Choose action: ", "recv")
        self.currentAction = self.actions[(int(num) - 1) % len(self.actions)]

    def ready(self):
        if self.currentAction != None:
            self.currentAction.ready()

    def action(self):
        if self.currentAction != None:
            self.currentAction.action()

    def reset(self):
        self.hp = self.MAX_HP

        self.defense = 0
        self.energy = 5

        self.currentAction = None
        self.states.clear()
    #====================================================
    def addState(self, state):
        if state.name in self.states: 
            self.states[state.name].reset()
        self.states[state.name] = state
        state.action()

    def updateState(self):
        values = list(self.states.values())
        for state in values:
            state.update()