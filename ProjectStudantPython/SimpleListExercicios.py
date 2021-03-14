from random import randint, random


def criaExibiLista():
    Lin = int(input("Quantidade de Linhas: "))
    Col = int(input("Quantidade de Colunas: "))
    M = []
    i = 0
    try:
        while i < Lin:
            M.append([])
            j = 0
            while j < Col:
                M[i].append(randint(0, 20))
                j += 1
            i += 1
        print("Esta é a lista M gerada")
        print("M =", M)

        print("Exibição em Matriz: ")
        i = 0
        while i < Lin:
            j = 0
            print('|', end='')
            while j < Col:
                print("{0:4}".format(M[i][j]), end='')
                j += 1
            print(" |")
            i += 1
    except ValueError:
        print("Valor deve ser do tipo INT")


# Function sequencia de Finobacci com laço FOR
def sequenciaFibonacci():
    print("Sequencia de fibonacci \n")
    N = 0
    while N < 2:
        try:
            N = int(input("Digite N(>1): "))
            if N < 2:
                print("Digite N >=2")
        except:
            print("O dado informado e invalido.")
    # criacao da lista com sequencia de fibonacci
    L = [0, 1]
    # realiza for no intervalo de valor de entrada menos 2 ( seria a quantidade de casas ja
    # ocupada pelos valores padroes da sequencia de fibonacci)
    for i in range(N - 2):
        L.append(L[i] + L[i + 1])
    print("Sequencia gerada", L)
    print("Fim do Programa")


def gerarListaOrdemCrescenteLoop():
    print("Gerador de lista em ordem Crescente \n")
    L = []
    x = int(input("Digite um valor: "))
    while x != 0:
        p = 0
        while p < len(L) and L[p] < x:
            L.insert(p, x)
            # a resposta do teclado incrementa o primeiro while, ao acrescentar um novo valor a x no final do laco
            x = int(input("Digite um valor: "))
    print("Lista gerada:", L)
    print("Fim do Programa")


def pesquisaSequencial():
    print("Lista Sequencial \n")
    N = int(input("Digite um valor para tamanho da Lista: "))
    x = int(input("Digite um valor: "))
    L = list(range(2, N + 1, 2))
    print(L)
    tam = len(L)
    aux1 = 2  # Obter metade do valor x/2 = 1/2
    while x != 0:
        ini = 0
        fim = len(L) - 1  # obter o valor final da lista (key do ultimo elemento inserido na lista ordenada)
        meio = (ini + fim) // 2  # obtem o indice do meio.
        while ini <= fim:
            print("Esse e o x: {0} ".format(x))
            print("Esse e o valor meio da lista: {0} ".format(L[meio]))
            print("Esse e o indice meio: {0} ".format(meio))
            if x == L[meio]:  # Verifica e o valor de x é igual ao valor do meio da lista
                print("O valor {0} já esta na lista".format(x))
                break  # Achou o valor

            if x < L[meio]:  # Verifica se x é menor que o valor do meio da lista.
                fim = meio - 1  # Atualizo o auxiliar fim informando que agora o final da minha lista é o valor de meio - 1
            else:
                ini = meio + 1
            meio = (ini + fim) // 2  # reseta o valor da variável para um novo indice no meio da lista
        else:
            print("{0} nao esta na lista".format(x))
        x = int(input("Digite o valor para x :"))


def algoritimoDeOrdenacao():
    print("Algoritimo de ordenação \n")
    L = [14, 55, 43, 1, 2, 76]
    print("Lista gerada:", L)

    mudouPosicao = 1
    while mudouPosicao:
        mudouPosicao = 0
        i = 0
        while i < len(L) - 1:  # trabalhando com o indice da lista
            # logo o tamanho da lista -1 (Lista tem de 0 há 5 (KEYS))
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                mudouPosicao = 1
            i += 1
        print("Estado Parcial de L:", L)
    print("\n Situacao Final")
    print("Lista Ordenada:", L)


# criaExibiLista()
# sequenciaFibonacci()
# gerarListaOrdemCrescenteLoop()
# pesquisaSequencial()
# algoritimoDeOrdenacao()


# INICIA AQUI OS EXERCICOS DO CAPITULO SOBRE TIPOS E ESTRUTURAS SEQUENCIAIS.

##########################################################################################
##########################################################################################
# 1. Escreva um programa que leia do teclado uma lista com tamanho de
# 10 elementos e exiba-a na tela na ordem inversa à ordem de leitura.

def ordemInversa():
    try:
        x = int(input("Informe o valor para lista: \n"))  # Recebo o valor para inserir na lista
        L = []
        tam = 10
        i = 0
        while len(L) < tam:  # Verifico se o tamanho da minha lista é = a variaval "tam"
            aux1 = x
            L.append(aux1)
            i += 1
            x = int(input("Informe o valor para lista: \n"))
        else:
            print("Lista ordem de inserção: ")
            print(L)
            print("\n")
            print("Lista ordem reversa: ")
            L.reverse()
            print(L)
    except ValueError:
        print("Informar um numero inteiro ex:1,2,3...")
    finally:
        print("Cheguei ao fim da minha operação. \n")
        print("")


# ordemInversa()

##########################################################################################
##########################################################################################
# 2. Escreva um programa que leia do teclado duas listas com tamanho 10, com números inteiros.
# Em seguida, o programa deve juntar as duas listas em uma única com o tamanho 20.
def mergedListas():
    try:
        # Variaveis
        L1 = []
        L2 = []
        L3 = []
        tam = 5
        i = 0
        while True:  # Realizo um while continuo. até que todas as interações necessárias
            # do meu laço, sejam realizadas.
            if len(L1) < tam:  # Verifico o tamanho da lista 1 com relação ao padrão adotado.
                value = int(input("Informe 10 valores para a primeira lista \n"))
                L1.append(value)
            elif len(L2) < tam:  # Verifico o tamanho da lista 2 com relação ao padrão adotado.
                value = int(input("Informe 10 valores para a Segunda Lista \n"))
                L2.append(value)
            else:
                L3 = L1 + L2  # Alimento uma terceira lista
                print(L3)
                print("\n")
                break

    except ValueError:
        print("Os Valores devem ser do tipo inteiro (INT)")
    finally:
        print("Lista Ordenada: \n")
        L3.sort()  # eexibo a lista com seus valores em ordem crescente
        print(L3)


# mergedListas()

##########################################################################################
##########################################################################################
# 3. Escreva um programa que preencha com números inteiros duas listas de-nominadas A e B
# com diferentes tamanhos nA e nB, respectivamente. Em seguida, o programa deve juntar as
# duas em uma única lista com o tamanho nA + nB. Exibir na tela a lista resultante.

def gerarListasDiferentesTamanhos():
    import random  # IMPORT necessário dentro da class para gerar numeros aleatórios (random.randint)

    try:
        # Variaveis
        tam1 = int(input("Informe o tamanho da primeira lista \n"))
        tam2 = int(input("Informe o tamanho da segunda lista \n"))
        i = 0
        L1 = []
        L2 = []
        L3 = []
        while True:  # Realizo um while continuo. até que todas as interações necessárias
            # do meu laço, sejam realizadas.
            if len(L1) < tam1:  # Verifico o tamanho da lista 1 com relação ao padrão adotado.
                value = random.randrange(0, 100)
                L1.append(value)
            elif len(L2) < tam2:  # Verifico o tamanho da lista 2 com relação ao padrão adotado.
                value = random.randrange(0, 100)
                L2.append(value)
            else:
                print("Lista 1 de tamanho {0} e elementos: {1} \n".format(tam1, L1))
                print("Lista 2 de tamanho {0} e elementos: {1} \n".format(tam1, L2))
                break

    except ValueError:
        print("Os Valores devem ser do tipo inteiro (INT)")

    else:
        # Após realização das condições do try. Realizo a operação abaixo
        L3 = L1 + L2  # Alimento uma terceira lista
    finally:
        # Finalizo. Exibo dados tratados no final
        if len(L3) > 0:
            print("Lista Ordenada: ")
            L3.sort()  # exibo a lista com seus valores em ordem crescente
            print(L3)

        callback = str(input(
            'Deseja Realizar novamente a operação S OU N'))  # Atribuo a possibilidade de retonar ao inicio da função.
        if callback == 'S':
            gerarListasDiferentesTamanhos()

        print("Registro de operações realizadas no METODO!!!")
        ###Interessante observar que o Finally, conta a quantidade de try_stmt
        ###realizadas dentro do metodo cujo o qual esta dentro de uma estrutura TRY
        ###interessante para percorrer algo e posteriormente, registrar processos realizados
        ###, para aquela instrução


# gerarListasDiferentesTamanhos()
##########################################################################################
##########################################################################################

# 4. Escreva um programa que leia uma lista com N números inteiros, em que N é um número inteiro
# previamente digitado pelo usuário. O programa não deve aceitar um número digitado que já esteja
# inserido na lista, sendo que, quando essa situação ocorrer, uma mensagem deve ser dada ao usuário.
# Por fim, exibir na tela a lista resultante

def gerarListaByTamanho():
    N = int(input('Informe o tamanho da lista: '))
    L1 = []
    aux1 = 0
    try:
        while aux1 < N:  # Verifico se o valor informado para tamanho de lista é maior que meu aux1
            x = int(input("Digite um valor para ser inserido na lista\n"))
            if x not in L1:  # Verifico se o valor existe na minha lista L1
                L1.append(x)
                aux1 += 1
            else:
                print("Valor já existe na lista.")
    except ValueError:
        print('Os Valores solicitados neste metodo devem ser do tipo INT.')
    else:
        callback = str(input(
            'Deseja Realizar novamente a operação S OU N'))  # Atribuo a possibilidade de retonar ao inicio da função.
        if callback == 'S':
            gerarListaByTamanho()
    finally:
        print(L1)  # Exibo o resultado final das minhas atividades
        ###Interessante observar que o Finally, conta a quantidade de try_stmt
        ###realizadas dentro do metodo cujo o qual esta dentro de uma estrutura TRY
        ###interessante para percorrer algo e posteriormente, registrar processos realizados
        ###, para aquela instrução


# gerarListaByTamanho()
##########################################################################################
##########################################################################################

##########################################################################################
##########################################################################################
# 4. Escreva um programa que leia do teclado dois números inteiros nA e nB e leia também duas
# listas denominadas A e B com os tamanhos nA e nB, respectivamente. Na leitura de cada uma
# das listas é obrigatório que não sejam aceitos valores repetidos. Em seguida, o programa deve
# juntar as duas em uma única lista R (resultante), tomando o cuidado de que R não tenha valores duplicados.

def gerarListasDiferentesTamanhosElementoUnico():
    import random  # IMPORT necessário dentro da class para gerar numeros aleatórios (random.randint)

    try:
        # Variaveis
        tam1 = int(input("Informe o tamanho da primeira lista \n"))
        tam2 = int(input("Informe o tamanho da segunda lista \n"))
        aux1 = 0
        aux2 = 0
        L1 = []
        L2 = []
        L3 = []

        while True:  # Realizo um while. até que todas as interações necessárias
            # do meu laço, sejam realizadas.
            if aux1 < tam1:  # Verifico o tamanho da lista 1 com relação ao padrão adotado.
                value = int(input("Digite um valor para ser inserido na primeira lista\n"))
                if value not in L1:
                    L1.append(value)
                    aux1 += 1
                else:
                    print("Valor já existe na lista 1.")
            elif aux2 < tam2:  # Verifico o tamanho da lista 2 com relação ao padrão adotado.
                value = int(input("Digite um valor para ser inserido na segunda lista\n"))
                if value not in L2:
                    L2.append(value)
                    aux2 += 1
                else:
                    print("Valor já existe na lista 2.")
            else:
                print("Lista 1 de tamanho {0} e elementos: {1} \n".format(tam1, L1))
                print("Lista 2 de tamanho {0} e elementos: {1} \n".format(tam1, L2))
                break

        L3 = L1 + L2  # Alimento uma terceira lista
    except ValueError:
        print("Os Valores devem ser do tipo inteiro (INT)")

    else:
        callback = str(input(
            'Deseja Realizar novamente a operação S OU N'))  # Atribuo a possibilidade de retonar ao inicio da função.
        if callback == 'S':
            gerarListasDiferentesTamanhosElementoUnico()
    finally:
        # Finalizo. Exibo dados tratados no final
        if len(L3) > 0:
            print("Lista Ordenada: ")
            L3.sort()  # exibo a lista com seus valores em ordem crescente
            print(L3)

        print("Registro de operações realizadas no METODO!!!")
        ###Interessante observar que o Finally, conta a quantidade de try_stmt
        ###realizadas dentro do metodo cujo o qual esta dentro de uma estrutura TRY
        ###interessante para percorrer algo e posteriormente, registrar processos realizados
        ###, para aquela instrução


# gerarListasDiferentesTamanhosElementoUnico()
##########################################################################################
##########################################################################################
# Escreva um programa que leia três dados de entrada: o primeiro termo, a razão e a quantidade
# de termos de uma P.A., todos números inteiros. O programa deve calcular todos os termos,
# colocando-os em uma lista, e exi-bi-la no final.

# função auxiliar, gera botão)
def functionCallBack():
    visualizarLog = str(input(
        'Deseja Visualizar log de operações/Exceções S OU N'))  # Atribuo a possibilidade de retonar ao inicio da função.
    return visualizarLog


def progressaoAritimetica():
    # Variáveis
    Q = int
    Termo = int
    Razao = int
    callback = str

    try:
        # ação do meu metodo valida/aloca valor em memoria.
        Q = int(input("Informe a quantidade de elementos que vai inserir: "))
        listaPA = []
        Count = 0
        while Count < Q:
            Termo = int(input("Informe o termo"))
            Razao = int(input("Digite a Razão: "))

            PA = Termo + Razao
            Count = Count + 1
            listaPA.append(PA)
        print("Lista Progressão Aritimetica")
        print(listaPA)

    except ValueError:
        print("Os Valores devem ser do tipo inteiro (INT)")
    else:
        callback = functionCallBack()
        if callback == 'S':
            progressaoAritimetica()
    finally:
        # Finalizo. Exibo dados tratados no final
        visualizarLog = functionCallBack()  # Função para chamar um input para solicitar dado
        if visualizarLog == 'S':
            # verifico se nenhum dos trés itens da tupla é do type int
            if int not in (type(Termo), type(Razao),
                           type(Q)):  # Alterar para is_string para identificar se alguns dos itens é do tipo string
                print("################LOG##############Os Valores devem ser do tipo inteiro (INT)\n")
        callback = str(input(
            'Deseja Realizar uma nova Operação? S OU N \n'))  # Atribuo a possibilidade de retonar ao inicio da função.
        if callback == 'S':
            progressaoAritimetica()

# Estudar with > finally essa funcionalidade permite gravar o logs do que foi executado
# no metodo em questão.

progressaoAritimetica()
##########################################################################################
##########################################################################################

# Escreva um programa que leia um número N obrigatoriamente entre 0 e 50 e, em seguida, leia
# N números reais em uma lista A. O programa deve separar os valores lidos em A em outras duas
# listas NEG e POS: a primeira contendo somente os valores negativos e a segunda contendo os valores
# positivos e zero. Apresentar na tela as listas NEG e POS e a quantidade de valores contidos em cada uma

# PAREI AQUI CONTINUAR LISTA DE EXERCICIO PAGINA 117
