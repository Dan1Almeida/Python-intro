print('**************************************')
print('*******Adivinhe qual é o número*******')
print('**************************************')


#Relembrar constantes e variáveis
NUMERO_SECRETO = 83 #constante
tentativa = input('Tente Acertar o número: ')
print(f'Você Digitou: {tentativa}')


try: #Estrutura do TRY
    tentativa_int = int(tentativa)
except ValueError:
    print(f'Valor Errado, informe um número inteiro')
    exit()
else:
    pass
finally:
    pass



if(NUMERO_SECRETO == tentativa_int):
    print('Você Acertou!!')
else:
    print('Você Errou')


print('GAME OVER')
print('Obrigado por participar')