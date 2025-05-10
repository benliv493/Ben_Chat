import socket
import threading
import queue
import time

addresses = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 59995))


def HandleUser(client, addr, msg):
    print('Connected from', addr, client)
    addresses.append(client)
    client.send('Connected to Server'.encode())
    while True:
        current_message = (client.recv(1024).decode())
        msg.put(current_message)
        time.sleep(1)
        current_message = ""


def Listening():
    while True:
        client, addr = server.accept()
        thread = threading.Thread(target=HandleUser, args=(client, addr, messages,))
        thread.start()


messages = queue.Queue()

thread2 = threading.Thread(target=Listening, args=())
server.listen()
thread2.start()
while True:
    print('here')
    msg = messages.get(timeout=240)
    msg1 = msg + '\n'
    print(msg)
    for client in addresses:
        try:
            client.send((msg1).encode())
        except Exception as e:
            print("error", e)
            addresses.remove(client)


