import gtts
from playsound import playsound

with open('falas.txt', 'r') as arquivo:
    for linha in arquivo:
        frase = gtts.gTTS(linha, lang='pt-BR')
        frase.save('frase.mp3')
        playsound('frase.mp3')
