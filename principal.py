from modelos import Produto, listar_produtos

def exibir_menu():
    print("============================")
    print("MENU DE PRODUTOS")
    print(" 0 - Para sair")
    print(" 1 - Para Cadastrar ")
    print(" 2 - Para Listar")
    print("============================")

def cadastrar():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço: "))
    categoria = input("Digite a categoria: ")

    produto = Produto(nome, preco, categoria)
    produto.salvar()

def mostrar ():
    for produto in listar_produtos():
        produto.exibir()

while True:
    opcao = input("Digite uma opção: ")

    if opcao == "0":
        break
    if opcao == "1":
        cadastrar()
    if opcao == "2":
        mostrar()
    else:
        print("Opção Inválida! Tente novamente.")