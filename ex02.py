'''Preencha um dicionário com as informações de 5 produtos.
- Utilize o nome do produto como chave e o preço como valor.
- Solicite os dados ao usuário.
Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50.00
Exemplo:
Veja um exemplo da estrutura do dicionário.
{'Caneta': 3.0, 'Pen Drive': 100.0, 'Teclado': 30.0}
'''

produtos = {}

for i in range(5):
    nome_produto = str(input("Digite o nome do produto: "))
    preco_produto = float(input("Digite o preço do produto: "))
    produtos[nome_produto] = preco_produto

for produto, preco in produtos.items():
    if preco > 50:
        print(f"{produto}: R${preco:.2f}")
