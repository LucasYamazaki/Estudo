import speech_recognition as sr
import pyttsx3



engine = pyttsx3.init()
rec = sr.Recognizer()
mercado = []
atividades = []
casa = []
editar = []

#Configurando fala.
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[-2].id)

#Setando a lista 'atividades' com o arquivo txt.
with open('tarefas.txt','r') as arquivo:
    for valor in arquivo:
        atividades.append(valor)

#Adicionar nova tarefa
def nova_trefa():
    with open('tarefas.txt','a') as arquivo:
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            fala("Qual tarefa deseja adicionar? ")
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language= "pt-BR")
        arquivo.write(str(texto) + '\n')
        atividades.append(texto)
        fala("Atividade adicionada com sucesso")

#Remover tarefa
def excluir_tarefa():
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        fala("Qual tarefa deseja excluir? ")
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language= "pt-BR")
        try:
            atividades.remove(texto + '\n')
            fala("Atividade excluida com sucesso")
            with open('tarefas.txt','w') as arquivo:
                for tarefa in atividades:
                    arquivo.write(str(tarefa))
        except Exception:
                fala("Atividade não encontrada")
                
    
def fala(texto):
    engine.say(texto)
    engine.runAndWait()



#Menu
print(atividades)
print("---Menu---")
print("1-Ver tarefas")
print("2-Adicionar tarefa")
print("3-Excluir tarefa")
print("4-Editar tarefa")
while True:
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        fala("Diga um comando: ")
        audio = rec.listen(mic)
        comando = rec.recognize_google(audio, language="pt-BR")
    if comando == "tarefas":
        with open('tarefas.txt','r') as arquivo:
            for valor in arquivo:
                print(valor)
                print(atividades)
    elif comando == "Adicionar tarefa":
        nova_trefa()
    elif comando == "excluir tarefa":
        excluir_tarefa()
    else:
        print("Comando inválido")