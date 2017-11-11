import socket
import threading
import sys
import pallindrome
import Database
import FileMAN
class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.sock.bind(('0.0.0.0', 8080))

        self.sock.listen(1)


    def handler(self,c, a):
        #global connections
        while True:
            data = c.recv(15000000)
            for connection in self.connections:
                #hel = pallindrome.pall(str(data, 'utf-8'))
                #Database.databaseStore(str(data, 'utf-8'),hel)
                #connection.send(hel.encode())
                check = FileMAN.storeImage(data,"trial")
                print(check)
                Database.databaseStore("trial",check)
                connection.send("\nSuccessful\n".encode())
            if not data:
                print(str(a[0])+':'+str(a[1]), "disconnected")
                self.connections.remove(c)
                c.close()
                break

    def run(self):
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c,a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(str(a[0])+':'+str(a[1]), "connected")


server = Server()
server.run()
