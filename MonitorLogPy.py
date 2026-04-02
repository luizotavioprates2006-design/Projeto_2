import random
import datetime

def menu():
    nome_arq = "log.txt"
    while True:
        print("MENU\n")
        print("1 - Gerar Logs")
        print("2 - Analisar Logs")
        print("3 - Gerar e analisa logs")
        print("4 - SAIR")
        opc = int(input("Escolha uma opção: "))
        if opc == 1:
            try:
                qtd = int(input("Quantidades de logs (Registros): "))
                gerarArquivo(nome_arq, qtd)
            except:
                print("Entrada inválida.")
        elif opc == 2:
            analisarLogs(nome_arq)
        elif opc == 3:
            try:
                qtd = int(input("Quantidade de logs (Registros): "))
                gerarArquivo(nome_arq, qtd)
                analisarLogs(nome_arq)
            except:
                print("Entrada Inválida")
        elif opc == 4:
            print("Até Mais!")
            break
        else:
            print("Opção Inválida")

def gerarArquivo(nome_arq, qtd):
    with open(nome_arq, "w", encoding="UTF-8") as arq:
        for i in range(qtd):
            arq.write(montarLog(i) + "\n")
    print("Log Gerado")

def montarLog(i):
    data      = gerarData(i)
    ip        = gerarIp(i)
    recurso   = gerarRecurso(i)
    metodo    = gerarMetodo(i)
    status    = gerarStatus(i)
    tempo     = gerarTempo(i)
    agente    = gerarAgente(i)
    protocolo = gerarProtocolo(i)
    tamanho   = gerarTamanho(i)
    return f'[{data}] {i} - {metodo} - {status} - {recurso} - {tempo}ms - {tamanho} - {protocolo} - {agente} - /home'
    
    def gerarData(i):
        base = datetime.datetime.now()
        delta = datetime.timedelta (seconds= i * random.rendint(5,20))
        return (base + delta).strftime('%d/%m/%Y %H:%M:%S')
    
def gerarIp(i):
   
    if i >= 20 and i <=50:
        return '203.120.45.7'
    else:
        return f'{random.randint(10,200)}.{random.randint(100,200)}.{random.randint(0,250)}.{random.randint(1,250)}'
    
   