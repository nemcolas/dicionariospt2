'''Exercício 03
Preencha um dicionário com os dados de 5 alunos.
- Utilize o ra do aluno como chave e uma lista de três notas como valor.
- Solicite os dados ao usuário.
Percorra o dicionário e exiba a média de cada aluno.
Exemplo:
Veja um exemplo da estrutura do dicionário.
{1901502: [10, 8, 7.5], 2002441: [6, 5, 7.5], 2001332: [5, 8, 9.5]}'''



alunos = {}

for i in range(5):
    ra = int(input("Digite o RA do aluno: "))
    notas = []
    for n in range(3):
        nota = float(input(f"Digite a nota do aluno: "))
        notas.append(nota)
    alunos[ra] = notas


print("Média de cada aluno:")
for ra, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"RA: {ra}, Média: {media:.2f}")


