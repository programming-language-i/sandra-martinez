import socket
import threading

HOST = "127.0.0.1"
PORT = 8000


def recibir_mensaje(conexion):
    while True:
        try:
            datos = conexion.recv(1024)

            if not datos:
                print("\nSe perdio conexion")
                break

            print(f"\n{datos.decode()}")
            print(">", end="", flush=True)

        except ConnectionResetError:
            print("Conexion terminada")
            break


nombre = input("Ingrese su nombre: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))

    print("Conectado al servidor")
    print("Escribe, mensaje. Usa '0' para salir")

    hilo = threading.Thread(target=recibir_mensaje, args=(cliente,), daemon=True)

    hilo.start()

    while True:
        mensaje = input("> ")

        if mensaje.lower() == "0":
            break

        cliente.sendall(f"{nombre}: {mensaje}".encode())
