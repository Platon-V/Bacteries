import time
import socket

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
main_socket.bind(("localhost", 7856))
main_socket.listen(5)
main_socket.setblocking(False)
print("Сервер создан")

players=[]
while True:
    try:
        conn, addr = main_socket.accept()
        print("Подключился", addr)
        main_socket.setblocking(False)
        players.append(conn)
    except BlockingIOError:
        pass
    for sock in players:
        try:
            data = sock.recv(1024).decode()
            print(data)
        except BlockingIOError:
            pass
        