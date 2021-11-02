import socket
import threading
import CompressAndDecompress
from  CompressAndDecompress import Compressed
class TCPserver():
    def __init__(self):
        self.server_ip='localhost'
        self.server_port = 9999
    def main(self):
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((self.server_ip, self.server_port))
        server.listen(1)
        print(f'[*] Listening on {self.server_ip}:{self.server_port}')
        while True:
            client, address = server.accept()
            print(f'[*] Accepted connection from {address[0]}:{address[1]}')
            client_handler =threading.Thread(target=self.handle_client, args=(client,))
            client_handler.start()

    def handle_client(self,client_socket):
        with client_socket as sock:
            request = sock.recv(1024)
            
           
            # print("data List",type(request))
            # # print(f'CypherText{dataList[0]}: Key{dataList[1]}')
            print("####################################################")
            
            print(f'[*] Received: {request.decode("utf-8")}')

            testString = request.decode("utf-8")
            testString = testString.split(',')
            print(f'CypherText{testString[0]} : Key:{testString[1]}')


            #Changing to integer to decompress
            # Received: int = int(request.decode("utf-8"))
            # print("Type of Received:>",type(Received))

            #1-calling compressAndDecompress
            #2-call Compress Class from compress and decompress
            # deletestring='test'
            #working code
            # changeData = Compressed(deletestring,Received)
            # DeData:str =changeData.decompress()
            # print("Decompressed Data  From client:>",DeData)
            sock.send(b'ACK')
            # toSend=bytes(request)
            # sock.send()


if __name__ == '__main__':
    Myserver = TCPserver()
    Myserver.main()