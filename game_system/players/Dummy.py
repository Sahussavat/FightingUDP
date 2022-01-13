
from random import randrange
from game_system.action.RightAtk import RightAtk
from game_system.action.LeftAtk import LeftAtk
from game_system.action.LeftBlock import LeftBlock
from game_system.action.RightBlock import RightBlock

class Dummy:

    MAX_HP = 100
    hp = MAX_HP

    defense = 0
    MAX_ENERGY = 3
    energy = MAX_ENERGY

    currentAction = None

    states = {}
    
    #====================================================
    def __init__(self, gameMain):
        self.name = "Dummy"
        self.gameMain = gameMain
        self.actions = [
                RightAtk(self, gameMain),
                LeftAtk(self, gameMain),
                LeftBlock(self, gameMain),
                RightBlock(self, gameMain),
                ]
    #====================================================
    def takeDamages(self, damages):
        self.hp = self.hp - (damages - (damages * self.defense/100))
        if self.hp < 0: self.hp = 0
        if self.isDead(): self.gameMain.getInstance().results\
            .append(f'{self.name} is Dead')

    def gainEnergy(self, energy):
        self.energy += energy
        if(self.energy > self.MAX_ENERGY): self.energy = self.MAX_ENERGY

    def isDead(self):
        return self.hp <= 0
    #====================================================
    def show_action(self):
        self.currentAction = self.actions[randrange(len(self.actions))]

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