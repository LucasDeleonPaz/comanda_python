from utils.json_handler import read_json, write_json, read_table_json, write_table_json
from management.tab_handler import calculate_tab

def main():
    
    oriencatacao = input("""O que você deseja fazer?
    1 - Cadastrar um novo produto
    2 - Listar todos os produtos 
    3 - Lançar consumo numa mesa
    4 - Valor total do consumo de uma mesa
    """)

    if int(oriencatacao) == 1:
        nome_produto = input("Digite o nome do produto: ")
        preco_produto = input("Digite o valor do produto: ")
        novo_produto = write_json("menu.json", {"name": nome_produto, "price": preco_produto})
        print(novo_produto)
        return nome_produto
    elif int(oriencatacao) == 2:
        lista_produtos = read_json("menu.json")
        print(lista_produtos)
        return lista_produtos
    elif int(oriencatacao) == 3:
        mesa = input("Qual a mesa: ")
        id_produto = input("Qual o id do produto: ")
        qtde_produto = input("Qual a quantidade do produto consumida: ")
        novo_lancamento = write_table_json(mesa ,{"id":int(id_produto),"amount":int(qtde_produto)})
        print(novo_lancamento)
        return novo_lancamento
    elif int(oriencatacao) == 4:
        mesa = input("Digite a mesa que deseja fecha a conta: ")
        valor = calculate_tab(mesa)
        print(valor)
        return valor
    else:
        print("Favor digitar uma ação válida")

if __name__ == "__main__":
    main()
    
