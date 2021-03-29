from ListaTelefonica import ListaTelefonica
import re
listaTelefonica = ListaTelefonica()  # instancia da listaTelefonica


def cadastrarContatoListaTelefonica(nome, telefone):#Criando function para Cadastro de nova lista
    '''
    Adicionar Contato na Lista Telefonica Encadeada
    :param: Nome, Telefone
    :return: result exec action
    '''

    regex = r"[^0-9]"
    subst = ""
    telefoneByRegex = re.sub(regex, subst, telefone, 0, re.MULTILINE)

    listaTelefonica.append(nome=nome, telefone=telefoneByRegex)
    return listaTelefonica


def visualizarListaTelefonica():
    '''
    Visualização de Lista Telefonica Encadeada
    :return: Lista
    '''
    print(listaTelefonica)

def deleteContatoListaTelefonica(condition, value):#Criando Function para Deletar contato da lista
    '''
    Excluir Contato na Lista Telefonica Encadeada
    :param: condition
    :return: result exec action
    '''
    if condition.upper() == 'N':
        listaTelefonica.removeByNome(value)
    elif condition.upper() == 'I':
        value = value - 1
        listaTelefonica.remove(value)