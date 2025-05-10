import socket
import threading
import getpass

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59995))

name = input("Username: ")


client.send((name + ' has joined the chat').encode())

name = name + ': '
print(client.recv(1024).decode())

def listening():
    while True:
        print(client.recv(1024).decode())


thread = threading.Thread(target=listening)
thread.start()

while True:
    message = name +input ('')
    client.send(message.encode())
