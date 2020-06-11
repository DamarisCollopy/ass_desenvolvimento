import errno
import psutil
import os
import stat
import time
from operator import itemgetter

def meu_switch():
    validacao = True
    while validacao:
        z = int(input("Menu : "
                      "\n 1 : Processos Ativos"# 1 Questao A 
                      "\n 2 : Processo PID " # 1 Qestao B, fiz tambem a memoria porcento do pid escolhido
                      "\n 3 : CPU" # 1 Questao C fiquei na duvida se era todo o sistema ou apenas no pid
                      "\n 4 : Executar Bloco de Notas" # 2 Questao
                      "\n 5 : Diretorio Informação" # 3 QUestao A
                      "\n 6 : Manipulando Texto"
                      "\n 7 : Soma Txt"
                      "\n 7 : Sistema Operacional e Processos"
                      "\n 8 : Diretorios" #questao TP4 e TP5
                      "\n 9 : Numero de Clocks" # questao TP5
                      "\n 10 :Informação sobre sub rede de IP especifico " # questao TP6
                      "\n 11 : Sair \n"))
        if z == 1:
            processo_ativo()
        elif z == 2:
            processo_pid()
        elif z == 3:
            cpu_porcentagem()
        elif z == 4:
            executar_bloconotas()
        elif z == 5:
            consulta = input("Diretorio :"
                             "1 Consulta "
                             "2 Criação de Diretorio")
            if consulta == '2':
                nome = input("Nome do diretorio: ")
                diretorio_bytes(nome)
            elif consulta == '1':
                nome = input("Entre com o nome do diretorio para consulta:")
                diretorio_bytes(nome)
            else :
                print("Opção Invalida !")
        elif z == 6:
            manipulando_texto()
        elif z == 7:
            soma_txt()
        elif z == 11:
            print("Programa encerrado")
            break
        else:
            print("opcao inválida")

# 1 Questao
# A) Obtenha a lista de processos executando no momento, considerando que o processo pode deixar de existir enquanto seu programa manipula suas informações;
def processo_ativo():
    for procurar in psutil.process_iter(['name', 'status']):
        if procurar.info['status'] == psutil.STATUS_RUNNING:
            dic_processos = {'Nome do Processo': procurar.info['name'], 'Status': procurar.info['status']}
            print(dic_processos)

#1 Questao
# B) Imprima o nome do processo e seu PID;
def processo_pid():

    pid = os.getpid()
    print("Nome do processo ", psutil.Process(pid).name(), "PID", pid,"Status:", psutil.Process(pid).status())

    # Memoria
    processo = psutil.Process(os.getpid())
    print("CPU porcentagem:", processo.cpu_percent(), "%")
    # conversao em MB
    memoria = processo.memory_info()[0] >> 20
    print("Memoria usada processamento: ", memoria, "MB")
    # rss ou [0] usado para encontrar a memoria dentro da lista Sistema Operacional Windows
    memoria_porcentagem = processo.memory_percent("rss")
    print("Memoria em porcentagem processo: ", memoria_porcentagem , "%")

#1 Questao
# C) Imprima também o percentual de uso de CPU e de uso de memória.
def cpu_porcentagem():

    x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']
    lista_cpu_percent = []
    lista_memoria = []
    # cpu_percent representa a utilização atual da CPU em todo o sistema como uma porcentagem.
    for i in range(0, 20):
        processo = psutil.Process()
        cpu = psutil.cpu_percent()
        memoria_porcentagem = processo.memory_percent("rss")
        lista_memoria.append(memoria_porcentagem)
        lista_cpu_percent.append(cpu)
        time.sleep(1)

    text = ''
    for x,n, a in zip(x,lista_cpu_percent, lista_memoria):
        text += '\n{} Segundos :  Porcentagem de Uso CPU {} %  Porcentagem de Uso de Memoria {} %'.format(x,n, a)
    print(text)


# 2 Questao Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo para executar o programa do sistema Windows bloco de notas (notepad) para abrir o arquivo.
def executar_bloconotas():
    # Cria um diretorio no qual você se encontra.

    nome = input("Nome do Arquivo texto")
    try:
        os.system(nome)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    print("Arquivo texto nao existe (%s)!" % (nome))

def criar_diretorio(nome):

    try:
        os.mkdir(nome)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    print("Diretorio já existe, não é possivel criar um diretorio ja existente (%s)!" % (nome))
    return nome
# 3 Questao
# A) gere uma estrutura que armazena o nome dos arquivos em um determinado diretório e a quantidade de bytes que eles ocupam em disco. Obtenha o nome do diretório do usuário.
def diretorio_bytes(nome):

    lista_os = []
    lista_nome = []
    for percorrer in os.listdir(nome):
        # Percorrer passa a ser o nome de cada arquivo
        s = os.stat(percorrer)
        # Selecionei dentro da tupla s os dados que queria, no caso a data da criacao/hora e o tamanho
        # Formatei a hora para modo legivel
        formatar_hora = time.ctime(s[stat.ST_MTIME])
        formatar_criacao = time.ctime(s[stat.ST_CTIME])
        tamanho = s.st_size
        # Converti os dados do tamanho
        converter_tamanho = conversao_bytes(tamanho)
        # Salvei em duas listas, para depois jogar em uma tupla
        lista_nome.append(percorrer)
        lista_os.append((converter_tamanho))
        # O "ctime", conforme relatado pelo sistema operacional. Em alguns sistemas (como Unix), é a hora da última alteração de metadados e,
        # em outros (como Windows), é a hora de criação (consulte a documentação da plataforma para obter detalhes).
        print("Nome do Arquivo : ", percorrer)
        print("Data da Criação:", formatar_criacao)
        # biblioteca os stat.St_MTIME funcao que mostra a ultima modificacao, usando a biblioteca time eu consigo formatar o numero apresentado em hora,dia,ano,dia da semana e mes por isso chamei de formatar a hora
        print("Data da modificação :", (formatar_hora))
        print("Tamanho Arquivo:",conversao_bytes(tamanho))
    # 3 Questao B) Ordene decrescentemente esta estrutura pelo valor da quantidade de bytes ocupada em disco (pode usar as funções sort ou sorted);
    # Coloquei em uma tupla os dados da lista
    # Sorted ordenei usando itemgetter como chave, selecionei o campo 1 do tamanho e usei o reverse para inverter
    ordenar = (list(zip(lista_nome,lista_os)))
    produto_sorted = sorted(ordenar, key=itemgetter(1), reverse=True)
    print("Lista Ordenada :", produto_sorted)

    # 3 Questao C) gere um arquivo texto com os valores desta estrutura ordenados.
    # Abri o arquivo no caso existente, mas se nao houver esse arquivo ele cria
    # Write ele escreve o conteudo criado pelo sorted ordenado
    # “a” (append - adiciona no fim no arquivo)
    # Close fecha o arquivo
    criar = open("texto.txt","a")
    criar.write(str(produto_sorted))
    criar.close()

# 4 Questao Escreva um programa em Python que leia um arquivo texto e apresente na tela o seu conteúdo reverso.
def manipulando_texto():

    texto = input("Entre com o nome do arquivo texto: ")
    try:
        # Criei um arquivo_novo para ir como destino o arquivo invertido, produto final reverse.txt
        arquivo_novo = open("reverse.txt","w")
        # Abrir um arquivo existente que quero inverter, recebe o comando do usuario
        arquivo = open(texto,"r")
        with arquivo as meu_arquivo:
            leitura = meu_arquivo.read()
        # Aqui pego o arquivo existente e inverto
        arquivo_invertido = leitura[::-1]
        # Escrevo esse arquivo invertido no novo destino
        arquivo_novo.write(arquivo_invertido)
        # Fecho o arquivo
        arquivo_novo.close()
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            print("Arquivo texto nao existe (%s)!" % (texto))
            raise
        pass

# 4 Questao  Soma de dois arquivos txt
def soma_txt():

    lista_a = []
    lista_b = []
    a = open("a.txt",'r')
    b = open("b.txt",'r')

    # Criei duas lista para poder comparar o comprimento entre elas e ver se tem a mesma quantidade de numero
    for x in a:
        lista_a.append(x)
    for i in b:
        lista_b.append(i)
    # Aqui compara se a lista tem o numero de itens igual caso nao ele adiciona mais 0
    # Erros que podem acontecer na execucao, na hora de criar o arquivo pulei linhas, o ultimo numero nao pode pular linha pq se nao a lista considera isso como posicao
    while len(lista_b) != len(lista_a):
        f = open("a.txt", "a")
        f.writelines('\n0')
        lista_a.append('0')
    # Faz a soma e escreve o resultado no arquivo resultado.txt
    with open("a.txt", "r") as f1, open("b.txt","r") as f2, open("resultado.txt","w") as f_out:
        num_sum = map(sum, zip(map(int, f1.readlines()), map(int, f2.readlines())))
        res = "\n".join(map(str, num_sum))
        f_out.write(res)
        print("Resultado da Soma :", res)

# Converter unidades
def conversao_bytes(n):

    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

if __name__ == "__main__":
    print(meu_switch())