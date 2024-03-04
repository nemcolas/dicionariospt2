'''Exercício 01
Preencha um dicionário com as informações de 5 pessoas.
- Utilize o cpf da passoa como chave e o nome como valor.
- Solicite os dados ao usuário.
Exemplo:
Veja um exemplo da estrutura do dicionário.
{'111.222.333-28': 'Paulo', '444.555.234-43': 'Ana', '000.345.543-8':
'João'}
'''

dc = {}

for n in range(5):
    cpf = int(input("Informe o cpf, somente números: "))
    nome = str(input("Informe o nome: "))

    dc[cpf] = nome

print(dc)

