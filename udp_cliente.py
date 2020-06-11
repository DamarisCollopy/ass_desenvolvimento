import socket,pickle

# AF_INET = IPv4
# SOCK_STREAM = TCP

host = socket.gethostname()
porta = 9991
destino = (host,porta)

cliente = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    # Chamada para dispertar o servidor, sendTo substitui o bind
    msg = 'Ola servidor '
    cliente.sendto(msg.encode('utf-8'), destino)
    # Arquivo sendo recebido pelo servidor
    bytes, servidor = cliente.recvfrom(1024)
    lista = pickle.loads(bytes)
    print(lista)
    break

# Tempo de espera 5 segundos
cliente.settimeout(5)

cliente.close()
