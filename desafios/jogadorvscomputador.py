from random import randint

computador = randint(1,10)
jogador = int(input("Informe um número entre 1 e 10: "))


if jogador == computador:
        print("Ambos os números foram iguais, parabéns! Você acertou")
        
if jogador > computador:
        valor_jogador_maior = jogador - computador
        print("O jogador passou em", valor_jogador_maior)
        
elif computador > jogador:
        valor_computador_maior = computador - jogador
        print("O jogador passou em", valor_computador_maior)
    