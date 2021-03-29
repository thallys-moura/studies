from Contato import Contato

class ListaTelefonica:
    def __init__(self): #Sobrecarga de Classe
        self.cabeca = None
        self.size = 0

    def __len__(self):
        return self.size

    def __setitem__(self, indice):
        pass

    def __delitem__(self, indice):
        pass

    def __getitem__(self, indice):  #Obtem Valor apartir do Indice da lista
        ponteiro = self.cabeca

        for i in range(indice):
            if ponteiro:
                ponteiro = ponteiro.proximo
            else:
                raise IndexError('index out of range.')
        if ponteiro:
            return ponteiro
        else:
            raise IndexError('index out of range.')

    def __repr__(self):
        r = '###################-IN9-################### \n\n'
        i = 1
        ponteiro = self.cabeca
        while (ponteiro):
            r += "##########" + str(i) + " - " + str(ponteiro.nome) +" - "+ str(ponteiro.telefone) +"########## \n"
            i+= 1
            ponteiro = ponteiro.proximo
        return r

    def __str__(self):
        return self.__repr__()

    def append(self, nome=None, telefone=None): #Adiciona Valor ao final da Lista
        if self.cabeca:  # Vefica se existe valor para aquela posição
            ponteiro = self.cabeca
            while ponteiro.proximo:
                ponteiro = ponteiro.proximo
            ponteiro.proximo = Contato(nome, telefone)
        else:
            self.cabeca = Contato(nome, telefone)  # Insere um no na lista

        self.size += 1

    def remove(self, indice):#Remove Indice da Lista
        ponteiro = self.cabeca
        ponteiroAnterior = ponteiro
        i = 0
        if indice == i:
            self.cabeca = ponteiro.proximo
        else:
            while ponteiro:
                if i == indice:
                    ponteiroAnterior.proximo = ponteiro.proximo
                    self.size = self.size - 1
                    break
                ponteiroAnterior = ponteiro
                ponteiro = ponteiro.proximo
                i+=1

    def removeByNome(self, value):#Remove Valor a partir do Nome
        ponteiro = self.cabeca
        ponteiroAnterior = ponteiro
        print(ponteiro.nome)
        if ponteiro.nome == value:
            self.cabeca = ponteiro.proximo
        else:
            while ponteiro:
                if ponteiro.nome == value:
                    self.size = self.size - 1
                    ponteiroAnterior.proximo = ponteiro.proximo
                    break
                ponteiroAnterior = ponteiro
                ponteiro = ponteiro.proximo

    def getIndiceByNome(self, value):
        #Retorna o indice do elemento na lista apartir do nome
        ponteiro = self.cabeca
        i=0
        if ponteiro.nome == value:
            return i
        else:
            while ponteiro.nome:
                if ponteiro.nome == value:
                    return i
                ponteiro = ponteiro.proximo
                i += 1

    def get(self, indice):
        ponteiro = self.cabeca

        for i in range(indice):
            if ponteiro:
                ponteiro = ponteiro.proximo
            else:
                raise IndexError('index out of range.')
        if ponteiro:
            return ponteiro
        else:
            raise IndexError('index out of range.')

