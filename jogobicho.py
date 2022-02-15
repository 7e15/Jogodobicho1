import sys
sys.path.append("./")
from bichos import numeros_bixo
import random


def jogar():
    print("Castor-de-Andrade: Olá boa praça! Veio jogar no bicho hoje né? Hehe")
    print("Castor-de-Andrade: Então vamos lá!")
    print("---------------------------------------------------------------")

    numero_sorteado = round(random.randrange(1, 101))

    chute: int = int(input("Escolha seu bixo digitando um número de 1-100 fera: "))
    print("Você apostou 10zão no ", chute)

    for animal, numeros in numeros_bixo.items():
        if chute in set(numeros):
            print(animal)
            break

    for animal_2, numeros in numeros_bixo.items():
        if numero_sorteado in set(numeros):
            break

    acertou = chute == numero_sorteado
    errou = chute != numero_sorteado

    if (acertou):
        print("Você acertou e ganhou no bicho! 500tão na mão! ")

    else:
        if (errou):
            print("Eita neném! Você errou!")
            print("O número sorteado era: ", numero_sorteado, animal_2)
            print("Castor-de-Andrade: Oh não, você perdeu!! xD HAHAHAHAHHA")

print(jogar())