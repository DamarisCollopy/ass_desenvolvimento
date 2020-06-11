import threading,time,random

# Execucao sequencial questao 8 A e B
a = [1,2,4,6]
b_sequencia = []
b_thre = []

def fatorial(n):
    fat = n
    for i in range(n-1,1,-1):
        fat = fat * i
    b_thre.append(fat)
    return(fat)

if __name__ == '__main__':
    tempo = time.time()
    # sequencialmente (sem concorrência)
    for x in a :
        b_sequencia.append(fatorial(x))
    # usando o módulo threading com 4 threads
    for i in a:
        t = threading.Thread(target=fatorial,args=(i,))
        t.start()
    # Esperar a threading ser concluida


    tempo_final = time.time()
    tempo_total = round(tempo_final - tempo,2)
    print("Observe o tempo decorrido para o processamento em sequencia e ou outro por threading, e a quantidade de threding e processos")
    print("Valores sequenciais: ", b_sequencia,  "Tempo de processamento:", tempo_total, "seg")
    print("Modulo Threading: ", b_thre, "Tempo de processamento:", tempo_total, "seg")

