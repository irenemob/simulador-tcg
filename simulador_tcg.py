# preparando inputs
# monstro 1

m1_nome = input('Digite o nome do monstro 1: ').upper()
m1_vida = int(input(f'Agora, digite os pontos de vida do {m1_nome}: ' ))
m1_ataque = int(input(f'Por fim, digite os pontos de ataque do {m1_nome}: '))

# validacao 1
if m1_vida <= 0 or m1_ataque <= 0:
    print('ERRO! Os pontos devem ser maiores que zero. Tente novamente!')
    quit()

# monstro 2
m2_nome = input('\nDigite o nome do monstro 2: ').upper()
m2_vida = int(input(f'Agora, digite os pontos de vida do {m2_nome}: '))
m2_ataque = int(input(f'Por fim, digite os pontos de ataque do {m2_nome}: '))
# validacao 2 
if m2_vida <= 0 or m2_ataque <= 0:
    print('ERRO! A vida e o ataque devem ser maiores que zero. Tente novamente!')
    quit()

#funcoes

def atacar(nome_atacante, ataque, nome_defensor, hp_defensor):
    novo_hp = hp_defensor - ataque
    
    if novo_hp < 0:
        novo_hp = 0
        
    
    print(f"\n{nome_atacante} atacou {nome_defensor} causando {ataque} de dano!")
    
   
    return novo_hp

def exibir_placar(nome1, hp1, nome2, hp2):
    print("=" * 30)
    print("       PLACAR ATUAL             ")
    print("=" * 30)
    print(f" {nome1}: {hp1} HP")
    print(f" {nome2}: {hp2} HP")
    print("=" * 30 + "\n")
print("\n    ")
print( '=' * 30)
print('Iniciando partida...')
print( '=' * 30)
#aplicar loop

while m1_vida > 0  and m2_vida > 0:
    m2_vida = atacar(m1_nome, m1_ataque, m2_nome, m2_vida)
    if m2_vida > 0:
        m1_vida = atacar(m2_nome, m2_ataque, m1_nome, m1_vida)
    print('\n  ')
    exibir_placar(m2_nome, m2_vida, m1_nome, m1_vida)
# resultados 
   
print( '=' * 30)
print('      O duelo encerrou!')
print( '=' * 30)
print('      RESULTADO DA PARTIDA:')  
print( '=' * 30)

if m1_vida <= 0:
    print(f"\nO monstro {m2_nome} é o vencedor do jogo!")
elif m2_vida <= 0:
    print(f"\nO monstro {m1_nome} é o vencedor do jogo!")

