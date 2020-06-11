# Cliente
import socket, pickle

# Criar o socket cliente:
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#  Definir o servidor e porta:
servidor = socket.gethostname()
porta = 9990
#  Arquivo que vai ser usado
nome_arquivo = input("Consulta de diretorio:")

try:

    cliente.connect((servidor, porta))

    cliente.send(nome_arquivo.encode('utf-8'))

    bytes = cliente.recv(1024)

    # Recebe um conjunto de bytes, preciso tratar a lista uso pickle
    # Converter bytes em uma lista
    lista = pickle.loads(bytes)
    print(lista)

    msg = input("Escreva fim para encerrar programa...")
    cliente.send(msg.encode('utf-8'))

    # Biblioteca padrao Exception
except Exception as erro:
    print(str(erro))

cliente.close()
