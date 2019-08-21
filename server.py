import socket
import threading


class server():
    def __init__(self, ip = "127.0.0.1", port = 9999):
        self.sock = socket.socket()
        self.addr = (ip, port)

    def startService(self):
        self.sock.bind(self.addr)
        self.sock.listen() 
        threading.Thread(target = self.accept, name = "accept").start()

    def accept(self):
        while True:
            sock1, addr = self.sock.accept()
            threading.Thread(target = self.rec, args = (sock1,)).start()

    def rec(self,sock):
        while True:
            data = sock.recv(1024)
            message = data.decode()
            print(message)

    def close(self):
        self.sock.close()
        


    
