class Contato: #DEFINIÇÃO ADOTADA PARA O NOME DADO AO OBJETO QUE SERA ELEMENTO DA LISTA
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.proximo = None
