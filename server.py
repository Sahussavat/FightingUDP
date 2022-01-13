from game_system.GameMain import GameMain
from game_system.Server_Socket import Server_Socket
from game_system.players.Dummy import Dummy

IP = "127.0.0.1"
PORT = 8000

Server_Socket.getInstance().server_socket.bind((IP, PORT))

print(f'Server is on')

GameMain.getInstance().players["Dummy"] = Dummy(GameMain.getInstance())


def on_game():
    while True:
        Server_Socket.getInstance().action("Will ye start?: ", "recv")
        GameMain.getInstance().vote_start_game(addr)

while True:
    username, conn, addr = Server_Socket.getInstance().action("Enter your name: ", "send")
    GameMain.getInstance().connectPlayer(username)
    on_game()

