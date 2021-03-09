from No import No
#sequencial = []
#insert elements in end point of list
class ListaEncadeada:
    #construtor
    #def define uma função
    def __init__(self):
        #topo da lista
        self.head = None
        self.size = 0
    def append(self, elemento):
        if self.head: # tem algum elemento ai
            #entao continue com a inserção (entra no else).
            #enquanto ponteiro.proximo == None
            #insere o proximo elemento na listaEncadeada
            ponteiro = self.head
            print(ponteiro.next)
            while(ponteiro.next):
                # Variavel Auxiliar (ponteiro) > recebe cabeca
                ponteiro = ponteiro.next
            ponteiro.next = No(elemento)
        else: # estamos inserindo o primeiro elemento na lista
              #primeiro elemento que relaciona o inicio da lista.
            self.head = No(elemento)
        self.size = self.size + 1
