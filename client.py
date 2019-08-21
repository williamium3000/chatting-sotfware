#!C:\Users\liyon\AppData\Local\Programs\Python\Python37\python.exe
import socket

client = socket.socket()
client.connect(("127.0.0.1",9999))
while True:
    try:
        data = input("请输入消息")
        client.sendall(data.encode())
    except Exception as e:
        print("send failure")