import multiprocessing,time,random
from multiprocessing import Queue

# 9 Teste todos os 3 programas da questão 8, capture os tempos de execução deles e compare-os, explicando os resultados de tempos.
# Varie o valor de N em 1.000.000, 5000.000, 10.000.000 (ou escolha números maiores ou melhores de acordo com a velocidade de processamento
# do computador utilizado para testes).
a = []
b = []
# Fila Queue, criar uma fila para o processamento
q = Queue()

def fatorial(n,q):
    fat = n
    for i in range(n-1,1,-1):
        fat = fat * i
    q.put(fat)
    return(fat)

if __name__ == '__main__':
    tempo = time.time()

    # 8 Questao usando o módulo multiprocessing com 4 processos
    n = int(input("Entre com o numero de processos: "))
    for x in range(n):
        a.append(random.randint(1,10))

    for i in a:
        t = multiprocessing.Process(target=fatorial,args=(i,q))
        t.start()
        # Esperar a threading ser concluida
        t.join()

# Enquanto a fila nao estiver vazia imprima
    while not q.empty():
        print("Fatorial :", q.get())

    tempo_final = time.time()
    print("Tempo de execucao", {round(tempo - tempo_final,2)}, "segundos")