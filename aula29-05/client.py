import socket

#snickcase = separado_por_anderline_e_tudo_minusculo 

def star_server(host: str, port: int):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    message = input('Type your message: ')
    client_socket.connect((host, port))
    client_socket.sendall(message.encode('utf-8'))

    client_socket.close()


if __name__ == '__main__':
    
    HOST = 'localhost' #IP do servidor
    PORT = 9000 #porta do servidor

    star_server(HOST, PORT)

