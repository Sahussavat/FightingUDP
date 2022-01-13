
import time
from game_system.Server_Socket import Server_Socket

class ResultPhase:

    def __init__(self, gameMain):
        self.gameMain = gameMain

    def action(self):
        Server_Socket.getInstance().action(next_mode="recv")
        results = self.gameMain.results
        results.sort(reverse=True)
        for result in results:
            Server_Socket.getInstance().action(result,"recv")
            time.sleep(0.5)
        self.gameMain.results.clear()

    def next_phase(self):
        self.gameMain.currentPhase = self.gameMain.endCheckPhase