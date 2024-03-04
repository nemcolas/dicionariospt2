# exemplo de dicionário
pessoas = {'name': 'Paulo',
           'age': 30,
           'email': 'paulo@email.com'}
print(pessoas)

# consulta um item especifico
print(pessoas['email'])
print(pessoas['name'])

# alterar um item
pessoas['name'] = 'Paulo Vieira'
print(pessoas)

# inserir um item
pessoas['job'] = 'Professor'
pessoas['city'] = 'São Paulo'
print(pessoas)

# remover um item
pessoas.pop('email')
print(pessoas)

# in - verifica se uma chave existe no dicionario
if 'job' in pessoas:
    print('Chave existente')
else:
    print('Chave inexistente')

# preenche o dicionario com input
alunos = {}                 # dicionario vazio
while True:
    ra = input('Digite o RA (digite 0 para sair): ')
    if ra == "0":               # finanlizar o loop
        break
    elif ra in alunos:          # verifica se a chave ja existe no dicionario
        print('RA ja esta cadastrado')
    else:
        nome = input('Digite o nome: ')
        alunos[ra] = nome       # insere chave e valor no dicionario
print(alunos)

# exemplo de operador ternario
print(alunos if len(alunos) > 0 else 'Dicionario vazio')

# percorrer as chaves do dicionário
for chave in alunos.keys():
    print(chave)

# percorrer os valores do dicionário
for valor in alunos.values():
    print(valor)

# percorrer os itens (chave e valor)
for chave, valor in alunos.items():
    print(f'RM{chave} - {valor}')


# Dicionario que armazena listas
alunos = {'123': ['Maria', '1TDSPC', '234.675.765-98'],
          '456': ['João', '1TDSPA', '123.456.789-00']}
print(alunos['123'])
print(alunos['123'][2])
alunos['123'][1] = '1TDSPX'
print(alunos)

# Lista que armazena dicionários
aluno1 = {'rm': '123', 'nome': 'Maria', 'cpf': '123.456.789-65'}
aluno2 = {'rm': '456', 'nome': 'João', 'cpf': '543.654.789-00'}
lista = [aluno1, aluno2]
print(lista)
print(lista[0]['nome'])

# Dicionario que armazena outros dicionario
alunos = {'123': {'nome': 'Maria', 'cpf': '123.456.789-00'},
          '456': {'nome': 'João', 'cpf': '444.555.666-98'}}
print(alunos)
print(alunos['123']['cpf'])
