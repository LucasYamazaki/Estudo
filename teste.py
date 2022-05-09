import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[-2].id)

engine.say('estudar\n')
engine.runAndWait()



for valor in atividades:
    arquivo.write(str(valor))