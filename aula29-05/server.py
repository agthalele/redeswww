import socket

#snickcase = separado_por_anderline_e_tudo_minusculo 

def star_server(host: str, port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen(1)

    print(f'Servidor iniciado em {host} : {port}')

    client_socket, adress = server_socket.accept()

    data = client_socket.recv(1024)
    message = data.decode('utf-8')

    client_socket.close()

    print(message)

if __name__ == '__main__':
    
    HOST = 'localhost' #IP do servidor
    PORT = 9000 #porta do servidor

    star_server(HOST, PORT)

