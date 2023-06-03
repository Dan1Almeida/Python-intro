from os import system
from random import randint
system('cls')

print('**************************************')
print('*******Adivinhe qual é o número*******')
print('**************************************')

NUMERO_SECRETO = randint(0,100)

pontos = 1000
acerto = False

print('Qual o Nível de Dificuldade?')
print('(1) Padawan | (2) Cavaleiro | (3) Mestre Jedi')
nivel = int(input('\n Defina o Nível: '))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
elif nivel == 3:
    total_de_tentativas = 5

pontos_a_perder = int(pontos / total_de_tentativas)
print(f'Sua Pontuação atual: {pontos}')


for rodada in range(1, total_de_tentativas+1):
#while rodada <= total_de_tentativas:
    tentativa = input('Tente Acertar o número: ')
    print(f'Você Digitou: {tentativa}')
    print(f'\nTentativa {rodada} de {total_de_tentativas}')
    # rodada += 1

    try: #Estrutura do TRY
        tentativa_int = int(tentativa)
    except ValueError:
        print(f'Valor Errado, informe um número inteiro')
        exit()
    else:
        pass
    finally:
        pass

    if (tentativa_int < 1 or tentativa_int > 100):
        print('Tentativa Inválida! Somente números de 1 a 100')
        continue

    acerto = NUMERO_SECRETO == tentativa_int
    ehmaior = NUMERO_SECRETO < tentativa_int
    ehmenor = NUMERO_SECRETO > tentativa_int

    if acerto:
        print(f'Você Acertou!!\nVocê fez {pontos} Pontos')
        break
    else:
        pontos_proximidade = 50 - abs(NUMERO_SECRETO - tentativa_int)
        pontos = pontos - pontos_a_perder + pontos_proximidade
        print('Você Errou')

        if ehmaior:
            print('Você Digitou número maior que o número secreto.')
        if ehmenor:
            print('Você Digitou número menor que o número secreto.')
        if (rodada < total_de_tentativas):
            print(f'Sua pontuação atual: {pontos}')
        else:
            print('\n------------------------------')

if not acerto:
    system('cls')
    print('GAME OVER!!!!!')
    print(f'O Número secreto é {NUMERO_SECRETO}')

print('Obrigado por participar')