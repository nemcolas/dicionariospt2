'''Conte a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é
a vogal e o valor é a quantidade de vezes que essa vogal aparece no texto.
Exemplo:
Para o texto abaixo:
'faculdade de tecnologia impacta'
A função deve retornar o seguinte dicionário:
{'a': 5, 'u': 1, 'e': 3, 'o': 2, 'i': 2}
'''


def contador_de_vogais(texto):
    vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for vogais in texto:
        if vogais in texto:
            texto[vogais]
            return vogais


frase = (str(input("Digita a frase: ")))

contador_de_vogais(frase)
