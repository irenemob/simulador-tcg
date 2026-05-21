# preparando inputs
# monstro 1
m1_nome = input('Digite o nome do monstro 1: ').upper()
m1_vida = int(input(f'Agora, digite os pontos de vida do {m1_nome}: ' ))
m1_ataque = int(input(f'Por fim, digite os pontos de ataque do {m1_nome}: '))

# validacao 1
if m1_vida <= 0 or m1_ataque <= 0:
    print('ERRO! A vida e o ataque devem ser maiores que zero. Tente novamente!')
    quit()

# monstro 2
m2_nome = input('\nDigite o nome do monstro 2: ').upper()
m2_vida = int(input(f'Agora, digite os pontos de vida do {m2_nome}: '))
m2_ataque = int(input(f'Por fim, digite os pontos de ataque do {m2_nome}: '))

# validacao 2 
if m2_vida <= 0 or m2_ataque <= 0:
    print('ERRO! A vida e o ataque devem ser maiores que zero. Tente novamente!')
    quit()