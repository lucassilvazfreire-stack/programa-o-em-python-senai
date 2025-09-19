print('SISTEMAS DE NOTAS')

nome= input('nome do aluno')
nota1 = float(input('nota1-'))
nota2 = float(input('nota2-'))
nota3 = float(input('nota3-'))
print()

media=(nota1 + nota2 + nota3) / 3
print(media)
print()

aprovado = media >=7
recuperacao = media >=5 and media <=6.9
reprovado = media <5

print(f'''
SITUAÇÃO DO ALUNO {nome}
APROVADO? - {aprovado}
RECUPERAÇÃO - {recuperacao}
REPROVADO - {reprovado}
''')
        