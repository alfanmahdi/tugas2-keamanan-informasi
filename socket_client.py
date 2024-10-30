import socket
from tugas1KI_desAlgorithm import encrypt_text, decrypt_text, rkb, rk

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    print("Connected to the server. Type 'bye' to exit.")
    message = input(" -> ")

    while message.lower().strip() != 'bye':
        encrypted_message = encrypt_text(message, rkb, rk)
        client_socket.send(encrypted_message.encode())

        data = client_socket.recv(1024).decode()
        decrypted_message = decrypt_text(data, rkb[::-1], rk[::-1])

        print("Received from other client before decrypt:", data)
        print("Received from other client:", decrypted_message)

        message = input(" -> ")
    client_socket.close()

if __name__ == '__main__':
    client_program()
