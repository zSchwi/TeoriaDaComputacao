# Estruturação basica da quintupla (estados, alfabeto, transições, estado inicial, e estados finais)
estados = []
alfabeto = []
func_transicao = {} #dicionario (basicamente um maps)
estado_inicial = ""
estados_finais = []


#TODO: Tentar modularizar a logica de verificar os estados

def verifica_transicoes(palavra, estado_atual):
    for simbolo in palavra:
        print(f"estado atual: {estado_atual}")
        print(f"entrada atual: {simbolo}")
        print(f"Proximo estado: {func_transicao[(estado_atual, simbolo)]}")
        estado_atual = func_transicao[(estado_atual, simbolo)]
        
        if estado_atual == None:
            print("Não reconhece")
            return 0
    return estado_atual



numero_automatos = int(input("Digite o numero de automatos que você quer testar: "))

while(numero_automatos > 0):

    # Entrada de dados
    estados = input("Digite os estados que compoem o AFD, com espaço entre eles: ").split()

    alfabeto = input("Digite o alfabeto desse AFD, com espaço entre eles: ").split()

    estado_inicial = input("Digite qual é o estado inicial: ")

    estados_finais = input("Digite quais são os estados finais: ").split()

    print("Informe as funções de transição: ")

    #Aqui passamos por cada simbolo associado a um estado anotando qual sera seu proximo estado
    for estado in estados:
        for simbolo in alfabeto:
            #na entrega retirar isso
            print(f"\t {simbolo}")
            print(f"{estado}\t------>\t", end="")
            proximo_estado = input()

            if proximo_estado == " ":
                func_transicao[(estado, simbolo)] = None
            else:
                func_transicao[(estado, simbolo)] = proximo_estado


    print("Insira a palavra a ser verificada: ")
    palavra = input()

    estado_atual = estado_inicial


    # for simbolo in palavra:
    #     print(f"estado atual: {estado_atual}")
    #     print(f"entrada atual: {simbolo}")
    #     print(f"Proximo estado: {func_transicao[(estado_atual, simbolo)]}")
    #     estado_atual = func_transicao[(estado_atual, simbolo)]
        
    #     if estado_atual == None:
    #         print("Não reconhece")
    #         break


    if verifica_transicoes(palavra, estado_atual) in estados_finais:
        
        print("A palavra é reconhecida")
    else:
        print("A palavra não pertence a linguagem")

    numero_automatos -= 1
