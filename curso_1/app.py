import os
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                    {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_programa ():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        """) 

def exibir_opcoes():
    print('1. cadastrar restaurante')
    print('2. listar restaurante')
    print('3. alternar o estado do restaurante')
    print('4. sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def voltar_menu_principal():
    input("\nDigite um tecla para voltar ao menu principal: ")
    main()

def opcao_invalida():
    print("Opção inválida!\n")
    voltar_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto)) #len = tamanho
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria
    
    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    '''

    exibir_subtitulo('Cadastro de novos restaurantes!')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')

    categoria = input(f'digite o nome da categoria {nome_do_restaurante}: ')

    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}

    restaurantes.append(dados_do_restaurante) #colocar o nome da lista

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_menu_principal()

def listar_restaurante():
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(17)} | {'Categoria'.ljust(15)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado' #metodo ternario em 1 linha
        print(f"- {nome_restaurante.ljust(17)} | {categoria.ljust(15)} | {ativo}")
        #ljust= espaçamento
        
    voltar_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')

    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")

    restaurante_encontado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontado = True
            restaurante['ativo'] = not restaurante ['ativo'] #vai inverter se o restaurante esta ativo ou inativo
            mensagem= f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante ['ativo'] else f'O restautante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontado:
        print('O restaurante não foi encontrado')

    voltar_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurante()

        elif opcao_escolhida == 3:
            alternar_estado_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system("cls")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

#try: Dentro do bloco try, você coloca o código que pode gerar uma exceção (um erro)

#except: Se uma exceção ocorrer dentro do bloco try, o fluxo do programa será desviado para o bloco except.

#se o usuário digitar algo que não pode ser convertido para um inteiro (como uma letra), o programa não irá quebrar.