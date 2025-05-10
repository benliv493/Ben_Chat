import socket
import threading
import time
import signal

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(('a8:93:4a:3c:ce:a4',6))

trigger_input = threading.Event()

name = input("Username: ")

print(client.recv(1024).decode())
client.send((name + ' has joined the chat').encode())

name = name + ': '

def SignalHandler(sig, frame):
    print('keyboard detected')
    trigger_input.set()

def listening():
    while not trigger_input.is_set():
        print(client.recv(1024).decode())
        

signal.signal(signal.SIGINT, SignalHandler)        
        

thread = threading.Thread(target=listening)
thread.start()
while True:
    while trigger_input.is_set():
        message = input('Your message... ')
        message = name + message
        client.send(message.encode())
        trigger_input.clear()
        
