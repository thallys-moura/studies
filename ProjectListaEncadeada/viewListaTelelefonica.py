from ModelsListaTelefonica import cadastrarContatoListaTelefonica, deleteContatoListaTelefonica, visualizarListaTelefonica


def viewListaTelefonica():
    '''
    Visualizacao/Acoes de Lista Telefonica
    Neste Método será possível: Cadastrar Contatos para a lista Telefónica ;
    Visualizar Contatos da lista;
    Excluir Contatos da Lista;
    :param: action
    :return: return result
    '''
    print("Bem vindo! Siga os passos abaixo para cadastrar os contatos da sua lista. \r")
    print("#        C - para Cadastrar um contato.     #\r")
    print("#        D - para deletar um contato.       #\r")
    print("#        V - para Visualizar a lista.       #\r")
    print("#        E - para Sair.                     #\r")

    print("Digite a opcao escolhida: \r")
    action = str(input())
    try:

        if action.upper() == 'C':
            print("##############       Cadastrar Novo Contato       #############\r")
            nome = str(input("Digite o nome do Contato"))
            telefone = str(input("Digite o numero do Contato"))
            result = cadastrarContatoListaTelefonica(nome, telefone)
        elif action.upper() == 'D':
            print("Informe Qual das operações de exclusão abaixo deseja realizar: \r")
            print("#        N - Para Excluir por Nome.       #\r")
            print("#        I - Para Excluir por Indice.     #\r")
            condition = str(input("Digite uma das opções listadas acima \r"))
            if condition.upper() == 'I':
                value = int(input("Informe o valor do indice do Contato \r"))
                if value and condition:
                    result = deleteContatoListaTelefonica(condition, value)
                    if result:
                        pass
            elif condition.upper() == 'N':
                value = str(input("Informe o Nome do Contato \r"))
                if value:
                    deleteContatoListaTelefonica(condition, value)


        elif action.upper() == 'V':
            visualizarListaTelefonica()
        elif action.upper() == 'E':
            pass

    except ValueError:
        print("{} invalid insert value".format(action))
    finally:
        if(action.upper() != 'E'):
            print("Deseja realizar uma nova operação? \r")
            print("#        S - para Sim.       #\r")
            print("#        N - para Não.       #\r")

            action_reework = str(input())
            if action_reework.upper() == 'S':
                print("\r\r")
                viewListaTelefonica()
        print("##############       Fim da Aplicação       #############\r")

viewListaTelefonica()


