import random
print('Digite o nome dos jogadores\n')
n1 = str(input('Jogador 1: '))
n2 = str(input('Jogador 2: '))
n3 = str(input('Jogador 3: '))
n4 = str(input('Jogador 4: '))
n5 = str(input('Jogador 5: '))
n6 = str(input('Jogador 6: '))
n7 = str(input('Jogador 7: '))
n8 = str(input('Jogador 8: '))
n9 = str(input('Jogador 9: '))
n10 = str(input('Jogador 10: '))
n11 = str(input('Jogador 11: '))
n12 = str(input('Jogador 12: '))
n13 = str(input('Jogador 13: '))
n14 = str(input('Jogador 14: '))
n15 = str(input('Jogador 15: '))
n16 = float(input('Valor da quadra: R$ '))
lista = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15]
sorteio = random.choice(lista)
print('\nGoleiro Time 1')
print(sorteio)
lista.remove (sorteio)
sorteio = random.choice(lista)
print('Defesa Time 1')
print(sorteio)
lista.remove (sorteio)
sorteio = random.choice(lista)
print('Ala Esquerdo Time 1')
print(sorteio)
lista.remove (sorteio)
sorteio = random.choice(lista)
print('Ala Direito Time 1')
print(sorteio)
lista.remove (sorteio)
sorteio = random.choice(lista)
print('Pivô Time 1')
print(sorteio)
lista.remove (sorteio)
sorteio = random.choice(lista)
print('Goleiro Time 2')
print(sorteio)
lista.remove (sorteio)
sorteio = random.choice(lista)
print('Defesa Time 2')
print(sorteio)
lista.remove (sorteio)
sorteio = random.choice(lista)
print('Ala Esquerdo Time 2')
print(sorteio)
lista.remove (sorteio)
sorteio = random.choice(lista)
print('Ala Direito Time 2')
print(sorteio)
lista.remove (sorteio)
sorteio = random.choice(lista)
print('Pivô Time 2')
print(sorteio)
print('Goleiro Time 3')
print(sorteio)
lista.remove (sorteio)
sorteio = random.choice(lista)
print('Defesa Time 3')
print(sorteio)
lista.remove (sorteio)
sorteio = random.choice(lista)
print('Ala Esquerdo Time 3')
print(sorteio)
lista.remove (sorteio)
sorteio = random.choice(lista)
print('Ala Direito Time 3')
print(sorteio)
lista.remove (sorteio)
sorteio = random.choice(lista)
print('Pivô Time 3')
print(sorteio)
valor_quadra = n16 / 15
print('\nValor da quadra para cada jogador:')
print(valor_quadra)
