import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("f8:fe:5e:1e:eb:e1", 6))

server.listen(1)

client, addr = server.accept()

try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
        message = input("enter message:")
        client.send(message.encode("utf-8"))
except OSError as e:
    pass

client.close()
server.close()
