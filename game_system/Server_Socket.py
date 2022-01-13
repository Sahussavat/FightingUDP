import socket
import pickle

class Server_Socket:
    
    IP = "127.0.0.1"
    PORT = 8000

    client_addr = None

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #=====================================================
    __instance = None

    @staticmethod
    def getInstance():
        if Server_Socket.__instance == None:
            Server_Socket()
        return Server_Socket.__instance

    def __init__(self):
        if Server_Socket.__instance != None:
            raise Exception()
        else:
            Server_Socket.__instance = self
    #=====================================================
    def action(self, text=" ", next_mode = "send"):
        if(not self.client_addr): 
            data, addr = self.server_socket.recvfrom(4096)
            self.client_addr = addr
            self.server_socket.sendto(pickle.dumps("hello"), self.client_addr)
        msg = pickle.dumps([text, next_mode])
        self.server_socket.sendto(msg, self.client_addr)
        data, addr = self.server_socket.recvfrom(4096)
        self.client_addr = addr
        return pickle.loads(data), self.server_socket, addr