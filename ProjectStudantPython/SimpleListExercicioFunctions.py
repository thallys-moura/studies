import time

#Este é um modelo de função recursiva
def numPrimo(P):
    if P <= 1:
        return "Error"
    elif P == 2:
        return 1
    elif P % 2 == 0:
        return 0
    else:
        raiz = P ** 0.5 #Verifica se é primo aplicando raiz quadrada no valor
        print(raiz)
        R = 1
        i = 3
        while i <= raiz and R != 0: #caso valor de i seja menor que o valor da raiz de P
                                    #Então retrna o resto da divisão como 1 = True, o numero é primo, pois resta 1
            R = P%i
            i=+2
        return R
#
# value = numPrimo(5)
# print(value)


####################################################################
def listasInterseções(L1, L2):
    LR = []
    for x in L1: # enquanto existir x na lista L1
        if x in L2: # se existir x na lista L2
            LR.append(x) # adiciono na lista R os valores de interseção.
        return LR
####################################################################
#Modelo de função recursiva:
def somaListaElementos(L):
    if L == []: # condição que para a recursividade do metodo
        return 0 #false
    else:
        return L[0] + somaListaElementos(L[1:]) #chamo a função novamente passando o meu array de novo,
                                                #porém fatiado
                                                #(L[1:] onde "1:" informo o fatiamento do total do array - 1 há sua esquerda)

# print("Inicio do programa")
# lista = [1,2,3,4,5,6,7,8,9,10]
# S = somaListaElementos(lista)
# print("Lista: ", end="")
# print(lista)
# print("Soma dos elementos de L = {0}".format(S))
# print("Fim do programa")
#####################################################################
#Função recursiva com algoritimo de busca binaria:
def buscaBinariaRecursiva(lista, valosBusca, ini, fim):
    if ini > fim:
        return 0
    meio = (ini+fim) // 2
    if valosBusca == lista[meio]:
        return 1
    elif valosBusca < lista[meio]:
        return buscaBinariaRecursiva(lista, valosBusca, ini, (meio-1)) #Caso valor seja menor que o do indice meio no laço atual
                                                                       #chamo novamente a função atribuindo um novo valor a fim
    else:
        return buscaBinariaRecursiva(lista, valosBusca, meio+1, fim) #Realizo a mesma atividade descrita a cima, com o diferencial de
                                                                     # ao contrario de subtrair, somo um novo valor para ini.



def functionRecursivaBuscaBinaria():
    print ("Inicio do Programa")
    Lista = [3, 8, 11, 14, 16, 19, 25, 29, 31, 37, 42, 46, 53, 58, 60, 63, 71, 82]
    X = int(input("Informe um valor para pesquisar na lista"))
    while X != 0:
        resultBusca = buscaBinariaRecursiva(Lista, X, 0, len(Lista))
        if resultBusca != 0:#Caso minha função retorne 0 responde a mesma ideia de um return false.
            print("Valor {0} está contido na lista {1}".format(X, resultBusca))
        else:
            print("{0} não sta na lista".format(X))
        X = int(input("Informe um valor para pesquisar na lista."))
    print("Fim do programa!")

#functionRecursivaBuscaBinaria()

###################################################################################################
##################################################################################################
#as funções informadas acima, trata-se de exemplos, reproduzido de um livro, avim de uma melhor absorvição
#no caso através da escrita.

#SEGUE AGORA UMA QUANTIDAD DE 10 QUESTÕES D EXERCICIOS PARA SER RESOLVIDO NO LIVRO.
####################################################################################################
####################################################################################################
#1. Escreva uma função que recebe um número inteiro como parâmetro de entrada e retorna o texto “PAR” ou “ÍMPAR”
def isParorImpar(X):
    """
        :param X: value type of int
        :return: return 1 = True Or 0 = False
    """
    if X % 2 == 0:
        return 1
    else:
        return 0

def consultaNumberParOrImpar():
    X = int(input("Informe o valor que deseja consultar: "))
    result = isParorImpar(X)
    if result == 1:
        print("Numero Par")
    else:
        print("Numero Impar")

#consultaNumberParOrImpar()

####################################################################################################
####################################################################################################
#Ultilize uma função para carregar uma lista contendo os N primeiros números primos, em que N
# é um número inteiro fornecido pelo usuário.

def numPrimo(lista_numeros):
    """
    :param P: value type of int
    :return: return 0 = false or 1 = true when number is prime
    """
    lista_divisores = [x for x in lista_numeros if x == 2 or x == 4 or x % 2 != 0]
    lista_numeros = lista_divisores.copy()
    print(lista_divisores)
    start_time = time.time()
    lista_primos = list()
    for number in lista_numeros:
        soma_divisores = 0
        for divisor in lista_divisores:
            if number % divisor == 0:
                soma_divisores += 1
            elif number < divisor:
                break
            if soma_divisores > 2:
                break
        if soma_divisores == 2:
            lista_primos.append(number)
    print(lista_primos)
    print(f'Duração da quarta versão: {time.time() - start_time:.3f}s')


def buscaListaNumerosPrimos():
    N = int(input("Informe o valor de N"))
    lista_numeros = [x for x in range(N)] # Gero uma lista com a quantidade de digitos informados
    result = numPrimo(lista_numeros)
    print(result)


#buscaListaNumerosPrimos()
####################################################################################################
####################################################################################################
#3. Escreva uma função que receba dois números inteiros A e B como parâme-tros de entrada e retorne 1 se A for divisível por B e 0 caso contrário.


def divisaoXY(X,Y):
    """
    Realiza opração aritimética de divisão

    :param X: value X
    :param Y: value Y
    :return: return 0 where % == 0  or 1 where % != 0

    """
    if X % Y == 0:
        return 1
    else:
        return 0

def execFunctionDivisao():
    print('Inicido do Programa', end='')
    X = int(input("Informe o valor para X"))
    Y = int(input('Informe o valor para Y'))
    result = divisaoXY(X,Y)
    if result == 1:
        print("divisão com sobra 0")

#execFunctionDivisao()

####################################################################################################
####################################################################################################
#4. Escreva uma função que receba um número inteiro N e retorne uma lista com os bits 0 e 1, que representam
# N convertido para binário. Não use nenhuma função Python de conversão para binários. Em vez disso, elabore
# uma lógica baseada no processo de divisões sucessivas
def encodeToBinary(listValueBinary , N):
    """
    Essa função é uma função recursiva, para conversão Decimal -> binario
    :param listValueBinary: []
    :param N: int
    :return: retorna uma lista, contendo a sequencia binaria da conversão
    decimal para binario
    """
    aux1 = N
    divisor = 2
    print(aux1)
    if aux1 % divisor == 1:
        listValueBinary.append(1)
        return encodeToBinary(listValueBinary, int(N/divisor))
    elif aux1 % divisor == 0 and N != 2:
        listValueBinary.append(0)
        return encodeToBinary(listValueBinary, int(N/divisor))
    elif N == 2:
        listValueBinary.append(0)
        listValueBinary.append(1)
        listValueBinary.reverse()
    return listValueBinary

def convertValueEncodeBynari():
    listValueBinary = []
    start_time = time.time()

    value = int(input("Informe um valor"))
    valueEncoded = encodeToBinary(listValueBinary, value)
    print(valueEncoded)
    print(f'Duração da quarta versão: {time.time() - start_time:.3f}s')

#convertValueEncodeBynari()

####################################################################################################
####################################################################################################
