idade = int(input('Sua idade:\n'))
Altura = float(input('Sua Altura:\n'))
Peso = float(input('Seu Peso:\n'))

if idade >= 18 and Altura >= 1.60 and Peso >= 70:
    print('Parabéns, vc é apto para entrar no quartel')
else:
    print('Você não está apto!')
