import socket

def server_program():
    host = socket.gethostname()
    port = 5000

    serversocket = socket.socket()
    serversocket.bind((host, port))

    serversocket.listen(3)
    conn, address = serversocket.accept()
    print("Connection from :"+str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print('User2 : '+str(data))
        data = input(' --> ')
        conn.send(data.encode())
    conn.close()

if __name__ == '__main__':
    server_program()


