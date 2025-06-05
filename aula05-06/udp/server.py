import socket

def star_server(host: str, port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_socket.bind((host, port))

    print(f'Server UDP iniciado em {host} : {port}')

    while True:
        data, adress = server_socket.recvfrom(1024)
        message = data.decode('utf-8')

        print(f'[CLIENT] : {message}')
        
                                   
if __name__ == '__main__':
    
    HOST = 'localhost' #IP do servidor
    PORT = 9000 #porta do servidor

    star_server(HOST, PORT)

