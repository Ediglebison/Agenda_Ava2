from Funcoes import Funcoes

agenda = Funcoes.carregar()

while True:
    print("1 - Incluir novo contato")
    print("2 - Buscar contato")
    print("3 - Editar contato")
    print("4 - Excluir contato")
    print("5 - Listar contatos")
    print("0 - Sair")
    opcao = int(input("Digite o numero referente a opção que deseja: "))

    if opcao == 1:
        Funcoes.incluir(agenda)
        Funcoes.salvar(agenda)
    elif opcao == 2:
        Funcoes.buscar(agenda)
    elif opcao == 3:
        Funcoes.editar(agenda)
        Funcoes.salvar(agenda)
    elif opcao == 4:
        Funcoes.excluir(agenda)
        Funcoes.salvar(agenda)
    elif opcao == 5:
        Funcoes.listar(agenda)
    elif opcao == 0:
        print("Sistema encerrado")
        Funcoes.salvar(agenda)
        break
    elif 1 < opcao > 5:
        print("Opção inválida!")
