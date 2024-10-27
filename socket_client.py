import socket
from tugas1KI_desAlgorithm import encrypt_text, decrypt_text, rkb, rk

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input
    encrypted_response = encrypt_text(message, rkb, rk)

    while message.lower().strip() != 'bye':
        client_socket.send(encrypted_response.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        decrypted_message = decrypt_text(data, rkb[::-1], rk[::-1])

        print('Received from server before decrypt: ' + data)
        print('Received from server: ' + decrypted_message)  # show in terminal

        message = input(" -> ")  # again take input
        encrypted_response = encrypt_text(message, rkb, rk)

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()