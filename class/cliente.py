import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect(("127.0.0.1", 8080))
    print("mi dirección ", cliente.getsockname)
    print("Conectado al servidor en ", cliente.getpeername)
    cliente.sendall("mensaje para servidor".encode("utf-8"))
    print("Esperando respuesta del servidor...", cliente.recv(1024).decode("utf-8"))