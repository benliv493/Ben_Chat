import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("a8:93:4a:3c:ce:a4", 5))

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
