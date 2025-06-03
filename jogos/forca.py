import random
#cria uma lista de palavras que seram sorteadas
palavras = ['python', 'programacao','computacao','aula', 'trabalhadores']

#escolhemos umas das palavras
palavra_sorteada = random.choice(palavras)

#criamos uma string com traços que representam as letras
palavra_escondida = '-' * len(palavra_sorteada)

print(palavra_escondida)

letra_adivinhadas = []
max_tentativas = 5

while True:
    print(palavra_escondida)

    letra = input('Digite uma letra: ')

    if letra in letra_adivinhadas:
        print('Voce ja digitou essa letra. Tente outra por favor')
        continue

    letra_adivinhadas.append(letra)


    if letra in palavra_sorteada:
        lista = []
        for indice in range(len(palavra_sorteada)):
            if letra == palavra_sorteada[indice]:
                lista.append(letra)
            else:
                lista.append(palavra_escondida[indice])
        palavra_escondida = ''.join(lista)
    else:
        max_tentativas -= 1
        print(f'Letra não encontrada. Voce tem mais {max_tentativas} tentativas')

    if palavra_escondida == palavra_sorteada:
        print('Parabens')
        break
    elif max_tentativas == 0:
        print('Voce perdeu')
        break