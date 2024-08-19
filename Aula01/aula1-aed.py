"""
Construir um algoritmo que contenhas 3 listas, cada lista contendo: 
    Nome de produtos
    Preço de cada produto
    Quantidade de cada produto
Construir um função para imprimir um dos produtos da lista e uma função para retirar um dos produtos da lista. as funções devem receber um parâmetro que será usado para acessar a posição dos itens das listas que serão impressos ou retirados

"""
def criar_listas():
    """Cria três listas vazias para armazenar os dados dos produtos."""
    nomes_produtos = []
    precos_produtos = []
    quantidades_produtos = []
    return nomes_produtos, precos_produtos, quantidades_produtos

def adicionar_produto(nomes, precos, quantidades, nome, preco, quantidade):
    """Adiciona um novo produto às listas."""
    nomes.append(nome)
    precos.append(preco)
    quantidades.append(quantidade)

def imprimir_produto(nomes, precos, quantidades, indice):
    """Imprime as informações de um produto específico."""
    print("Produto:", nomes[indice])
    print("Preço:", precos[indice])
    print("Quantidade:", quantidades[indice])

def remover_produto(nomes, precos, quantidades, indice):
    """Remove um produto específico das listas."""
    nomes.pop(indice)
    precos.pop(indice)
    quantidades.pop(indice)

# Exemplo de uso:
nomes, precos, quantidades = criar_listas()

# Adicionando alguns produtos
adicionar_produto(nomes, precos, quantidades, "Maçã", 2.50, 10)
adicionar_produto(nomes, precos, quantidades, "Banana", 1.80, 15)
adicionar_produto(nomes, precos, quantidades, "Laranja", 3.00, 8)

# Imprimindo o segundo produto
imprimir_produto(nomes, precos, quantidades, 1)

# Removendo o primeiro produto
remover_produto(nomes, precos, quantidades, 0)

# Imprimindo a lista atualizada
for i in range(len(nomes)):
    imprimir_produto(nomes, precos, quantidades, i)



