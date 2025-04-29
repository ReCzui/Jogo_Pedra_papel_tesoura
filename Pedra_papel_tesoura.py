import random
from random import randint

resultados = {(1, 1): 'Empate',
              (1, 2): 'Jogador venceu',
              (1, 3): 'Computador venceu',
              (2, 1): 'Computador venceu',
              (2, 2): 'Empate',
              (2, 3): 'Jogador venceu',
              (3, 1): 'Jogador venceu',
              (3, 2): 'Computador venceu',
              (3, 3): 'Empate'}

placar = {'Empate': 0,
          'Jogador venceu': 0,
          'Computador venceu': 0}

itens = ['Papel', 'Pedra', 'Tesoura']

placar_jogador = []
placar_computador = []

print('-=' * 20)
print('     PAPEL | PEDRA | TESOURA      ')
print('-=' * 20)
while True:
    computador = randint(1, 3)

    print('\033[36m1 - Papel | 2- Pedra | 3- Tesoura\033[m')

    jogador = int(input('\033[1mEscolha uma opção:\033[m '))
    if jogador not in [1, 2, 3]:
        print('Opção inválida, tente novamente!')
        continue

    print()

    escolha_jogador = itens[jogador - 1]
    escolha_computador = itens[computador - 1]
    print('=' * 40)
    print(f'Você escolheu: \033[35m{escolha_jogador}\033[m')
    print(f'Computador escolheu: \033[34m{escolha_computador}\033[m')

    resultado = resultados[(jogador, computador)]

    if resultado in placar:
        placar[resultado] += 1
        print(f'\033[1m{resultado}\033[m')
        if resultado == 'Jogador venceu':
            placar_jogador.append(resultado)
        elif resultado == 'Computador venceu':
            placar_computador.append(resultado)

        print()
        print(f'\033[1mPLACAR:\033[m \nJogador: \033[31m{len(placar_jogador)}\033[m \nComputador: \033[31m{len(placar_computador)}\033[m')

    print('=' * 40)

    continuar = input('Quer jogar novamente? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        print('Programa encerrado!')
        break
    elif continuar != 'S':
        print('Opção inválida, tente novamente!')





