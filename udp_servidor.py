import socket,psutil,pickle,time
# Questao 7

# IP Local gethostname()
host = socket.gethostname()
porta = 9991
destino = (host,porta)
# UDP - socket.SOCK_DGRAM
# AF_INET = IPv4
servidor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# Bind apenas no servidor, o cliente utiliza o sendTo para abrir o socket
servidor.bind(destino)
print((f"Servidor {host} experando conexao na porta {porta}"))

disco = psutil.disk_usage('/')
disco_lista = {'Hora Inicio ':time.ctime(),'Disco Total': (disco.total / 1024 ** 3, "GB"), 'Disco Usado': (disco.used / 1024 ** 3, "GB"),
                'Disco Livre': (disco.free / 1024 ** 3, "GB")}

while True:
    # mensagem recebida do cliente, para abrir o canal entre eles
    (msg, cliente) = servidor.recvfrom(1024)
    mensagem = msg.decode('utf-8')
    print(mensagem)
    # tempo de espera 5 segundos
    servidor.settimeout(5)
    break
# Envio do arquivo
informacao_bytes = pickle.dumps(disco_lista)
servidor.sendto(informacao_bytes,cliente)
servidor.close()

