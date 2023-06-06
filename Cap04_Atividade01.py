from random import randint

def imprime_abertura():
    print("*" * 28)
    print("Jogo da Forca ".center(28,"-"))
    print("*" * 28)

def carrega_palavra_secreta():
    arquivo = open('frutas.txt', "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    sorteio = randint(0, len(palavras))

    palavra_secreta = palavras[sorteio]
    return palavra_secreta

def init_letras_acertadas(palavra_secreta):
    # list comprehension: [ _ , _ , _ , _ , _ ]
    return [ '_' for letra in palavra_secreta]

def gg():

    imprime_abertura

    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = init_letras_acertadas(palavra_secreta)
    
    morreu = False
    acertou = False
    erros = 0


    while (not morreu and not acertou):
        print(letras_acertadas) 
        tentativa = input('Qual a Letra? ').strip().lower()

        index = 0 
        if tentativa in palavra_secreta:

            for letra in palavra_secreta:

                if (tentativa == letra):
                    letras_acertadas[index] = letra
                index += 1 
        else:
            erros += 1
            morreu = erros == 7
            print ("Você Errou a Letra")

        acertou = '_' not in letras_acertadas


    if acertou:
        print('Você Venceu')
    else:
        print('Você Perdeu')

    print('\nObrigado Por Participar')

if __name__ == '__main__':
    gg()