import socket
import threading
from tugas1KI_desAlgorithm import encrypt_text, decrypt_text, rkb, rk

clients = []

def handle_client(conn, address):
    print("Connection from:", address)
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break

            decrypted_message = decrypt_text(data, rkb[::-1], rk[::-1])
            print(f"Message from {address} before decrypt: {data}")
            print(f"Message from {address}: {decrypted_message}")

            for client in clients:
                if client != conn:
                    encrypted_response = encrypt_text(decrypted_message, rkb, rk)
                    client.send(encrypted_response.encode())
        except:
            break

    conn.close()
    clients.remove(conn)
    print(f"Connection closed from: {address}")

def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)

    print("Server is running... Waiting for connections.")
    while True:
        conn, address = server_socket.accept()
        clients.append(conn)
        threading.Thread(target=handle_client, args=(conn, address)).start()

if _name_ == '_main_':
    server_program()