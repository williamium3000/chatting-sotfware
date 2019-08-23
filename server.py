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
        '''
            返回一个四/五元列表，包含（！【0】则为撤回消息报文）聊天id【0】发送时间【1】发送者id【2】发送内容【3】
        '''
        while True:
            data = sock.recv(1024)
            message = data.decode()
            message = message.strip()
            return message.split("|")

    def close(self):
        self.sock.close()
        


    
