import socket

class MyConnection():

    def __init__(self, PORT, HOST=''):
        self.HOST = HOST
        self.PORT = PORT
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def server(self):
        self.sock.bind((self.HOST, self.PORT))
        self.sock.listen(1)
        conn,addr = self.sock.accept()
        print(conn)
        print(addr)
        print(conn.recv(1024).decode())
        conn.close()
        self.sock.close()

    def client(self):
        self.sock.connect((self.HOST,self.PORT))
        self.sock.send(input("Mensaje: ").encode())
        self.sock.close()

def main():
    print("1. SERVER")
    print("2. CLIENT")
    option_menu = int(input("What do you want? ")) - 1
    host = input("HOST: ")
    port = int(input("PORT: "))
    newConnection = MyConnection(port, host)
    functions = [newConnection.server, newConnection.client]
    functions[option_menu]()

main()
