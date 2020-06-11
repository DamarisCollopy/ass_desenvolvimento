import socket, os, pickle

# 6 Questao Escreva um programa cliente e servidor sobre TCP em Python em que:

# AF_INET = IPv4
# SOCK_STREAM = TCP
lista_nome = []
host = socket.gethostname()
porta = 9990
# Usado para TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind((host, porta))
# Escutar concexao usado para TCP
servidor.listen()
print((f"Servidor {host} experando conexao na porta {porta}"))

# Uma funcao criada para coletar os dados em uma lista
def solicitar_consulta(nome_arquivo) :
    for percorrer in os.listdir(nome_arquivo):
        lista_nome.append(percorrer)
    return lista_nome

while True:
    (cliente, endereco) = servidor.accept()
    print(f"Conectado a {endereco}...")

    msg = cliente.recv(2048)
    nome_arquivo = msg.decode('utf-8')
    print(f"Solicitado o arquivo {nome_arquivo}...")
    # Envia a solicitacao, antes usa o pickle para transformar o arquivo
    diretorio = solicitar_consulta(nome_arquivo)
    informacao = pickle.dumps(diretorio)
    cliente.send(informacao)

    msg = cliente.recv(4)
    if msg.decode('utf-8') == 'fim':
        msg = "Programa encerrado"
        fim = pickle.dumps(msg)
        cliente.send(fim)
        break

    cliente.send(msg)

cliente.close()
servidor.close()
