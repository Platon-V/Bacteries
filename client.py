import socket

main_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY, 1)
main_socket.connect(('localhost',7856))

while True:
    main_socket.send("Привет".encode())
