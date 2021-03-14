##Importando bibliotecas usadas nas estruturas
import math
from random import randint


# FUNCTION SIMPLES REALIZA SOMA DE 2 VARIAVEIS
def somaSimples():
    #instancia as variáveis
    valorX = input("Informe o valor de X: ")
    valorY = input("Informe o valor de Y: ")
    #converto o tipo de dado para inteiro (int)
    valorZ = float(valorX) + float(valorY)

    #conjuto de exibição dos dados relativos a ação solicitada.
    print("Esses são os tipos dos meus valores para realizar operação {0} {1}".format(type(valorX), type(valorY)))
    print("Esse é o tipo do valor de Z: {0}".format(type(valorZ)))

    #soma dos valores aredondado
    print(valorZ)

# FUNCTION SIMPLES REALIZA CALCULO PARA OBTER FATURAMENTO
def faturamentoSimples():
    #instancia as variáveis
    valorX = input("Informe o valor Fixo: ")
    valorY = input("Informe o valor de Vendas: ")
    #instancia da variável comissão fixada em 6%
    comissao = 6/100
    sumXY = float(valorX) + float(valorY)
    #Calcula o valor total de X + Y * k(comissao)
    fat = sumXY * comissao
    print("Esse é o faturamento do més: {0:.2f}".format(fat))

# FUNCTION SIMPLES REEALIZA CALCULO PARA ACHAR ÁREA DE UM TRIANGULO (BASEE*ALTURA)
def areaTrianguloSimples():
    #instancia as variáveis
    valorX = input("Informe o valor da base: ")
    valorY = input("Informe o valor da Altura: ")
    area = float(valorX) * float(valorY)
    print("Essa é sua base {0}".format(area))

# FUNCTION SIMPLES REALIZA CALCULO PARA SALÁRIO BRUTO
def salarioBrutoSimples():
    valorX = float(input("Informe o valor em R$ da sua hora trabalhada: "))
    valorY = float(input("Informe a quantidade de horas trabalhadas: "))
    valorZ = float(input("Informe a quantidade de horas extras trabalhadas: "))
    valorHoraExtra = (valorX*2)*valorZ
    valorTotalHorasNormais = valorX*valorY
    print(valorHoraExtra)
    print(valorTotalHorasNormais)
    valorTotal = valorHoraExtra + valorTotalHorasNormais

    print("Seu salário bruto é de: {0:.2f}".format(valorTotal))

def operacoesAletorias():
    A=4
    B=5
    C=1
    x1 = 1
    y1 = 1
    x2 = 4
    y2 = 5
    #Calcula o Valor de R
    valorR = float((B+A)/2)
    print("Valor de F {0:.2f}".format(valorR))
    #Calcula o valor de X
    #INICIADO O USO DA LIB MATH -> FUNCTION SQRT(Raiz Quadrada)
    valorX = float((-B + math.sqrt((B**2)-(4*4*1)))/2*4)
    print("Esse é o valor de X: {0:.2f}".format(valorX))

# FUNCTION SIMPLES REALIZA CALCULO PARA IDENTIFICAÇÃO DE NUMEROS PARES/IMPARES
def parOuImpar():
    X = int(input("Digite o Valor de X: "))
    #exemplo de while
    while X != 0:
        if X % 2 == 0:
            print("print %d é par: " % X)
        elif X == "F":
            print("Até mais")
        else:
            print("print %d é impar: " % X)
        X = int(input("Digite o Valor de X: "))

# FUNCTION SIMPLES REALIZA CALCULO PARA PROGRESSÃO ARITIMETICA
def progressaoAritimetica():
    Q = int(input("Informe a quantidade de elementos que vai inserir: "))
    P = int(input("Digite o primeiro termo: "))
    R = int(input("Digite a Razão: "))

    Cont = 0
    while Cont <= Q:
        PA = P + R
        print("termo {:d} da PA {:d}".format(P, PA))
        P = int(input("Digite o primeiro termo: "))
        Cont = Cont + 1


# FUNCTION TOTALIZAÇÃO DE VALORES
def totalizacaoValores():
    Soma = 0
    Qtde = 0
    x = 1
    while x != 0:
        x = int(input("Digite X: "))
        if x <= 0:
            continue
        elif x != 0:
            Soma = Soma + x
            Qtde = Qtde + 1

    print("Total de valores digitados = %d" % Soma)
    print("Quantidade de valores = %d" % Qtde)

# FUNCTION VERIFICA NUMEROS PRIMOS
def verificaNumeroPrimo():
    N = int(input("Digite o valor para N: "))
    i = 2
    while i < N:
        R = N % i
        if R == 0:
            print("{} não é primo ".format(N))
            #Encerra o laço while
            break
        else:
            print("{} é primo".format(N))
    else:
        print("{} é primo".format(N))

#Function que tem como ideia uma possível substituição do Dowhile
#caso seja neecessário executar um conjunto de codigos onde a
#execução da condição seja pós loop (ao final do laço.)
def SubstitionDoWhile():
    while True:
        condicao = None
        #Codigo
        if condicao:
            break


def testClausulaTry():
    #Instancia a variável
    try: #Executa bloco de condições para os valos informados
        A = int(input("Digite um valor para A: "))
        B = int(input("Digite um valor para B: "))
        R = A/B
        print("O Resultado de R: {}".format(R))

        # Caso não seja possível executar o bloco por completo,
        # É retornado a exceeção para o bloco informado
        #Importante ressaltar que a exceção pode ser retornada de forma generica (Qualquer erro no bloco de erro, segue uma mensagem padrão)
        #OU Atribui-se a chamada para um dos erros padrão de core do python
    except ValueError:
        print("Digite números inteiros para A e B")
    except ZeroDivisionError:
        print("B ou A não pode ser Zero")
    except:
        print("Erro Desconhecido")


def testTryCompleto():
    #Instancia Variável
    N = 0
    #While testa a estrutura try completa
    while N < 100 or N > 500:
        try:
            S = input("Digite N no intervalo [100, 500]: ")
            N = int(S)
        except:
            print("{} não é o número.".format(S))
            N = 0
        else:
            if N < 100 or N > 500:
                print("O valor {} lido está fora do intervalo".format(N))
            else:
                print("O valor Lido {} está ok.".format(N))
        finally:
            print("Tchau")

#Função ultilizando de uma estrutura completa de try > except > else > finally
#recebe um valor, logo em seguida, cria uma quantidade de numeros random, e soma o total destes.
def TotalConjuntoValores():
    intervaloA = 1
    intervaloB = 50
    total = 0
    try:
        N = int(input("Informe o valor de N"))
    except ValueError:
        print("Digite números inteiros para A e B")
    except ZeroDivisionError:
        print("B ou A não pode ser Zero")
    except:
        print("Erro Desconhecido")
    else:
        count = 0
        while count < N:
            valueRandom = randint(intervaloA,intervaloB)
            total += valueRandom
            print("esse é o valor {}".format(valueRandom))
            count = count + 1
        print("O valor totalizado é: {}".format(total))
    finally:
        print('até mais!!!!!')

#Function sequencia de Finobacci
def sequenciaFibonacci():
    try:
        N = int(input("Informe o valor de N: "))
    except ValueError:
        print("Erro Invalido")
    else:
        i = 0
        aux1 = 0
        aux2 = 1
        fibonnaci = "0, 1, "
        while i < N-2:
                aux3 = aux1+aux2
                fibonnaci += "{}, ".format(aux3)
                print("esse é o valor {}".format(fibonnaci))
                aux1 = aux2
                aux2 = aux3
                i += 1

def classificacaoTriangulo():
    try:
        print("Informe o valor dos 3 lados do triangulo")
        A = float(input("Valor de A: "))
        B = float(input("Valor de B: "))
        C = float(input("Valor de C: "))
    except ValueError:
        print("Valor Digitado é invalido")
    else:
        AB = int(A+B)
        AC = int(A+C)
        BC = int(B+C)
        if AB == AC & AC == BC:
            print("Esse é um triangulo de todos os lados congruentes, Logo: Equilatero")
        elif AB == AC and AB != BC:
            print("Esse é um triangulo de todos os lados congruentes, Logo: Isosceles")
        elif AB != AC and AB != BC:
            print("Esse é um triangulo de todos os lados congruentes, Logo: Escaleno")
    finally:
        print("Erro não identificado")


#Função Simples para identificar se o valor é maior ou menor com relação ao segundo valor
def numeroMaiorOuMenor():
    NumA = None
    NumB = None
    try:
        NumA = int(input("Informe um numero para A: "))
        print("Perfeito...")
        NumB = int(input("Agora Informe um numero para B"))
    except ValueError:
        print("Valor informado é invalido")
    else:
        if NumA > NumB:
            print("A é maior que B")
        elif NumB > NumA:
            print("B é maior que A")
        elif NumB == NumA:
            print("Os numeros são equivalentes!")
    finally:
        print("Obrigado até mais")


def caterogiriasPeso():
    pessoaNome = input("Informe o nome do atleta: ")
    pesoAtleta = float(input("Informe o peso em Kg do atleta: "))

    try:
        while True:
            if(pesoAtleta < 65.0):
                print("O lutador {0} pesa {1} e se enquadra na categoria Ligeiro".format(pessoaNome, pesoAtleta))
            elif pesoAtleta >= float(65.0) & pesoAtleta < float(72.0):
                print("O lutador {0} pesa {1:.2f} e se enquadra na categoria Leve".format(pessoaNome, pesoAtleta))
            elif pesoAtleta >= 72.0 & pesoAtleta < 79.0:
                print("O lutador {0} pesa {1:.2f} e se enquadra na categoria Ligeiro".format(pessoaNome, pesoAtleta))
            elif pesoAtleta >= 79.0 & pesoAtleta < 86.0:
                print("O lutador {0} pesa {1:.2f} e se enquadra na categoria meio-médio".format(pessoaNome, pesoAtleta))
            elif pesoAtleta >= 86.0 & pesoAtleta < 93.0:
                print("O lutador {0} pesa {1:.2f} e se enquadra na categoria médio".format(pessoaNome, pesoAtleta))
            elif pesoAtleta >= 93.0 & pesoAtleta < 100.0:
                print("O lutador {0} pesa {1:.2f} e se enquadra na categoria Meio-Pesado".format(pessoaNome, pesoAtleta))
            else:
                print("O lutador {0} pesa {1:.2f} e se enquadra na categoria Pesado".format(pessoaNome, pesoAtleta))
            break

    except ValueError:
        print(ValueError)
    finally:
        print("Obrigado por usar nosso sistema de cadastro.")
#executando as functions
#soma()
#faturamentoSimples()
#areaTrianguloSimples()
#salarioBrutoSimples()
#operacoesAletorias()
#parOuImpar
#progressaoAritimetica()
#progressaoAritimetica()
#totalizacaoValores()
#verificaNumeroPrimo()
#testClausulaTry()
#testTryCompleto()
#TotalConjuntoValores()
#sequenciaFibonacci()
#classificacaoTriangulo()
#numeroMaiorOuMenor()
#caterogiriasPeso()


###############################################################################
############################ESSES FORAM ALGUNS EXERCICIOS DO LIVRO PYTHON3: CONCEITOS E APLICAÇÕES.
##################################################################################
