import speech_recognition as sr

rec = sr.Recognizer()
mercado = []
atividades = []
casa = []
editar = []

#Setando a lista 'atividades' com o arquivo txt.
with open('tarefas.txt','r') as arquivo:
    for valor in arquivo:
        atividades.append(valor)

#Adicionar nova tarefa
def nova_trefa():
    with open('tarefas.txt','a') as arquivo:
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            print("Pode falar: ")
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language= "pt-BR")
        arquivo.write(str(texto) + '\n')
        atividades.append(texto)

#Remover tarefa
def remover_tarefa():
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Diga a tarefa para remover: ")
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language= "pt-BR")
    with open('tarefas.txt','w') as arquivo:
        try:
            atividades.remove(texto)
            print("Atividade removida")
            for valor in atividades:
                arquivo.write(str(valor) + '\n')
        except Exception:
                print("Atividade não encontrada")
                for valor in atividades:
                    arquivo.write(str(valor) + '\n')
    

#Menu
print("---Menu---")
print("1-Ver tarefas")
print("2-Adicionar tarefa")
print("3-Remover tarefa")
print("4-Editar tarefa")
while True:
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Diga um comando: ")
        audio = rec.listen(mic)
        comando = rec.recognize_google(audio, language="pt-BR")
    if comando == "Ver tarefas":
        with open('tarefas.txt','a') as arquivo:
            for valor in arquivo:
                print(valor)
    elif comando == "Adicionar tarefa":
        nova_trefa()
    elif comando == "excluir tarefa":
        remover_tarefa()
    else:
        print("Comando inválido")