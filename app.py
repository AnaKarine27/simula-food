import os

restaurantes = [{'nome': 'Chiquinho Sorvetes', 'categoria': 'Sorveteria', 'ativo': False},
                {'nome': 'Burger King', 'categoria': 'Hamburgueria', 'ativo': True},
                {'nome': 'Montana Pizzaria', 'categoria': 'Pizzaria', 'ativo': False}]

def exibir_nome_do_programa():
    '''Essa função exibe o nome do programa'''
    print('SIMULA FOOD\n')

def exibir_opcoes():
    '''Essa função exibe o menu de opções'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função encerra a aplicação'''
    exibir_subtitulo('App encerrado!')

def voltar_ao_menu_principal():
    '''Essa função retorna ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    '''Essa função é usada quando o usuário digitar uma opção inválida'''
    print('Opção inválida!')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função exibe os subtitulos dos menus'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria
    
    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função exibe a lista de restaurantes cadastrados'''
    exibir_subtitulo('Lista de restaurantes:')

    print(f'{'NOME DO RESTAURANTE'.ljust(22)} | {'CATEGORIA'.ljust(20)} | STATUS')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categ_restaurante = restaurante['categoria']
        ativo_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'➭ {nome_restaurante.ljust(20)} | {categ_restaurante.ljust(20)} | {ativo_restaurante}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função alterna o status dos restaurantes para ativo ou inativo'''
    exibir_subtitulo('Alternando estado do restaurante.')
    
    nome_restaurante = input('Digite o nome do restaurante que desaja alternar o estado: ')   
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')
            
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função é utilizada para selecionar a opção escolhida'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Essa função exibe a tela inicial da aplicação'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()