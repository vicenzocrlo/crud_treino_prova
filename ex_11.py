lista_produtos = []

def Cadastrar(produto):
    lista_produtos.append(produto)
    print("Seu produto foi cadastrado com sucesso!")

def Listar():
    print("======= Produtos =======\n")
    if not lista_produtos:
        print("A sua lista está vazia!")
    else:
        for i, produto in enumerate(lista_produtos, 1):
            print(f"{i}. {produto}")
            
def Buscar(busca):
    for i in lista_produtos:
        if i == busca:
            print(f"\n Produto encontrado!: {i}")
            encontrado = True
            break
    if not encontrado:
        print("Produto não foi encontrado!")

def Editar():
    nome_antigo = input("Digite o nome do produto que deseja alterar: ")
    
    if nome_antigo in lista_produtos:

        indice = lista_produtos.index(nome_antigo)
        
        novo_nome = input(f"Digite o novo nome para '{nome_antigo}': ")
        
        lista_produtos[indice] = novo_nome
        print("Produto atualizado com sucesso!")
    else:
        print("Produto não encontrado para atualização.")

def Excluir():
    produto = input("Digite o nome do produto para excluir: ")
    
    if produto in lista_produtos:
        lista_produtos.remove(produto)
        print(f"'{produto}' removido com sucesso!")
    else:
        print(" Erro: Produto não encontrado na lista.")

def Sair():
    print("Saindo...")
    
menu = """
======= Cadastro de Produtos =======

[1] Cadastrar Produtos
[2] Listar Produtos
[3] Buscar Produto
[4] Editar Produto
[5] Excluir Produto
[6] Sair

"""
while True:
    print(menu)
    entrada = int(input("Seja bem vindo, digite a opção da operação que você deseja realizar em nosso sistema: "))

    if entrada == 1:
        produto = input("Digite o nome do produto que você deseja cadastrar: ")
        Cadastrar(produto)

    elif entrada == 2:
        Listar()
    
    elif entrada == 3:
        busca = input("Digite o nome do produto que você deseja buscar: ").strip()
        Buscar(busca)

    elif entrada == 4:
        Editar()

    elif entrada == 5:
        Excluir()

    elif entrada == 6:
        Sair()
        break

    else:
        print("Opção inválida, digite novamente!")