# encontre o numero  python Jogo_adivinhar_numeros.py

import random

print("Seja Bem vindo, Bora acertar o numero")

# Função para repetir o numero ate o usuario acertar 

while True:    

# Gerar o numero aleatorio

    n1 = random.randint(1, 50)
    print(n1)

    chances = 5 

    print("Pense em um numero de 1 a 50")
    print("Voce terá 5 Chances, Pense bem ao escolher o numero rsrs... ")

    #loop para ir diminuindo as tentativas conforme o jogador erre o numero 
    while chances > 0:

        #tentativas do usuario
        palpite = input("Vamos começar!!! Jogador, escolha um Numero! ")

        #validação se digitou um numero valido
        if not palpite.isdigit():
            print("Isso não é um número valido! Digite novamente um numero entre 1 e 50")
            continue

        #converter palpite para inteiro
        palpite = int(palpite)

        #verificar se esta no intervalo estipulado
        if palpite < 1 or palpite > 50:
            print("o numero {} esta fora do intervalo, Digite um numero entre 1 e 50!".format(palpite))
            continue

        #chances_restantes 
        chances -= 1

        # verificar se o Jogador acertou 

        if palpite == n1:
            print("PARABENS! voce acertou o seu palpite {} é o numero que o computador escolheu".format(palpite))
            print("Numero que o computador escolheu", n1)
            print("Seu palpite", palpite)
            break
        elif palpite < n1:
            print("Voce errou. Vou te dar uma dica, o numero é maior que {}".format(palpite))
            
        else:
            print("Voce errou. Vou te dar uma dica, o numero é menor que {}".format(palpite))


        print("Voce ainda tem {} tentativas. Digite um numero novamente: ".format(chances))
    
    else:
        print("Não foi dessa vez, o numero correto era {}. ".format(n1))
    
    jogar_novamente = input("Quer Jogar de novo? (s/n)  ").lower()

    if jogar_novamente != "s":
        print("Obrigado e até a proxima!")
        break


                






    
    