import socket
from tugas1KI_desAlgorithm import encrypt_text, decrypt_text, rkb, rk

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break

        decrypted_message = decrypt_text(data, rkb[::-1], rk[::-1])
        print('From connected user before decrypt: ' + data)
        print("From connected user: " + decrypted_message)
        data = input(' -> ')
        encrypted_response = encrypt_text(data, rkb, rk)
        conn.send(encrypted_response.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()