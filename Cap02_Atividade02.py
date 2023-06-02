from os import system
system('cls')

print('**************************************')
print('*******Adivinhe qual é o número*******')
print('**************************************')

rodada = 1
total_de_tentativas = 3

NUMERO_SECRETO = 83 #constante

while rodada <= total_de_tentativas:
    tentativa = input('Tente Acertar o número: ')
    print(f'Você Digitou: {tentativa}')
    print(f'\nTentativa {rodada} de {total_de_tentativas}')
    rodada += 1

    try: #Estrutura do TRY
        tentativa_int = int(tentativa)
    except ValueError:
        print(f'Valor Errado, informe um número inteiro')
        exit()
    else:
        pass
    finally:
        pass

    acerto = NUMERO_SECRETO == tentativa_int
    ehmaior = NUMERO_SECRETO < tentativa_int
    ehmenor = NUMERO_SECRETO > tentativa_int

    if acerto:
        print('Você Acertou!!')
        break
    else:
        print('Você Errou')

        if ehmaior:
            print('Você Digitou número maior que o número secreto.')
        if ehmenor:
            print('Você Digitou número menor que o número secreto.')

if not acerto:
    system('cls')
    print('GAME OVER')

print('Obrigado por participar')