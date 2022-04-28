palavra = 'forca'
digitadas = []
chances = 5
while True:
    letra = input("Digite uma letra: ")
    if len(letra) > 1:
        print("Mais de uma letra? Sério?... Digite só uma!")
        continue
    digitadas.append(letra)

    if letra in palavra:
        print(f"BOA!! A letra {letra} tem na palavra")

    else:
        print(f"Pena, a letra {letra} não pertence a palavra")
        digitadas.pop()
        chances -= 1
    if chances <=0:
        print('Você perdeu!')
        break

    palavra_temporaria = ''
    for letra_palavra in palavra:
        if letra_palavra in digitadas:
            palavra_temporaria += letra_palavra
        else:
            palavra_temporaria += '*'

    if palavra_temporaria == palavra:
        print('Parabéns!! Você acertou.')
    else:
        print(palavra_temporaria)
        print(f'Chances restantes: {chances}')