from array import array
from game_system.players.Player import Player
from game_system.phases.ActionPhase import ActionPhase
from game_system.phases.EndCheckPhase import EndCheckPhase
from game_system.phases.ResetPlayer import ResetPlayer
from game_system.phases.ResultPhase import ResultPhase
from game_system.phases.UpdateStatePhase import UpdateStatePhase 
from game_system.Server_Socket import Server_Socket

class GameMain:
    currentPhase = None

    isGameEnd = False
    players = {}
    results = []

    vote_start = {}
    #=====================================================
    __instance = None

    @staticmethod
    def getInstance():
        if GameMain.__instance == None:
            GameMain()
        return GameMain.__instance

    def __init__(self):
        if GameMain.__instance != None:
            raise Exception()
        else:
            GameMain.__instance = self
            self.resultPhase = ResultPhase(self)
            self.resetPlayer = ResetPlayer(self)
            self.endCheckPhase = EndCheckPhase(self)
            self.updateStatePhase = UpdateStatePhase(self)
            self.actionPhase = ActionPhase(self)
    #=====================================================
    def start_game(self):
        self.currentPhase = self.actionPhase
        while not self.isGameEnd:
            self.currentPhase.action()
            self.currentPhase.next_phase()
        self.currentPhase.action()
        self.isGameEnd = False

    def vote_start_game(self, addr):
        if(addr[0] in self.vote_start): 
            del self.vote_start[addr[0]]
        else: self.vote_start[addr[0]] = addr[0]

        Server_Socket.getInstance().action(f"Has vote {len(self.vote_start)}/1", "recv")
        vote_count = len(self.vote_start)
        if vote_count == 1:
            self.vote_start = {}
            self.start_game()
            Server_Socket.getInstance().action(f" ", "send")

    def connectPlayer(self, name):
        self.players[name] = Player(name, self)

    def getPlayers(self):
        return list(self.players.values()) 
    #=====================================================
            