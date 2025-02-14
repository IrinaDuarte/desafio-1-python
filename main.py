# missão 1

nota = 3

if nota >= 6:
    print('Aprovado')
else:
    print('Reprovado')

# missão 2

aluno = input('Seu nome:')
idade = input('Sua idade:')

if idade >= '16':
    print('Pode votar')
else:
    print('Não pode votar')

# missão 3

nota = 89

if nota >= 90:
    print('Parabéns, você tirou A')
elif nota >= 80:
    print('Muito bem, você tirou B.')
elif nota >= 70:
    print('Bom trabalho, você tirou C.')
elif nota >= 60:
    print('Fique atento, você tirou D.')
else:
    print('Estude um pouco mais, você tirou F.')

# missão 4

Numero1 = float(input('Primeiro número:'))
Numero2 = float(input('Segundo número:'))

print(Numero1 + Numero2)

# missão 5

usuário = input('Usuário:')
senha = input('Senha:')

if senha == 'Python123':
    print('Acesso Liberado')
else:
    print('Acesso Negado')

# missão 6

contador = 8

while contador <= 10:
    print(contador)
    contador += 1

# missão 7

números = [8, 3, 10, 1, 5]
números_em_ordem = sorted(números)
print(números_em_ordem)

# missão 8

nomes_alunos = ('Ana', 'Bruno', 'Carla', 'Daniel', 'Eduardo')
print(nomes_alunos[0])
print(nomes_alunos[4])

# missão 9

Número = int(input('Valor:'))
print(Número * 2)


# missão 10

nome = 'Ana'
print(len(nome))
