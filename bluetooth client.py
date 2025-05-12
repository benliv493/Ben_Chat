import socket
import threading
import time
import signal

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(('f8:fe:5e:1e:eb:e1',6))

trigger_input = threading.Event()

print('Press Ctrl + C to enter a message')
print('NOTE: Once you do this, you must send your message before you can see incoming messages')
name = input("Username: ")

print(client.recv(1024).decode())
client.send((name + ' has joined the chat').encode())

name = name + ': '

def SignalHandler(sig, frame):
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
        
