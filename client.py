import socket
import pickle

IP = "127.0.0.1"
PORT = 8000

username = "bob"

addr = (IP, PORT)
mode = "send"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto(pickle.dumps("next"), addr)
data, server_addr = client_socket.recvfrom(4096)

print(pickle.loads(data))

addr = server_addr

while True:

    if(mode == "send"):
        data, addr = client_socket.recvfrom(4096)
        if not data: continue
        data = pickle.loads(data)
        print(data[0], end='')
        client_socket.sendto(pickle.dumps(input()), addr)
        mode = data[1]
    elif(mode == "recv"):
        data, addr = client_socket.recvfrom(4096)
        if not data: continue
        data = pickle.loads(data) 
        print(data[0])
        client_socket.sendto(pickle.dumps("next text"), addr)
        mode = data[1]