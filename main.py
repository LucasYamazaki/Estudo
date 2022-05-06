atividades = []

#Setando a lista 'atividades' com o arquivo txt.
with open('tarefas.txt','r') as arquivo:
    for valor in arquivo:
        atividades.append(valor)

def nova_trefa():
    with open('tarefas.txt','a') as arquivo:
        valor = str(input("Digite uma tarefa: "))
        arquivo.write(str(valor) + '\n')
        atividades.append(valor)
def remover_tarefa():
    selecionar = str(input("Digite o nome da tarefa que quer remover: ")).strip()
    with open('tarefas.txt','w') as arquivo:
        for valor in atividades:
            if valor == selecionar:
                atividades.remove(selecionar)
                print("Atividade removida")
                for valor in atividades:
                    arquivo.write(str(valor) + '\n')
            else:
                print("Atividade não encontrada")
#    try:
#        atividades.remove(selecionar)
#        print("Atividade removida.")
#    except Exception:
#        print("Atividade não encontrada.")

print("---Menu---")
print("1-Ver tarefas")
print("2-Adicionar tarefa")
print("3-Remover tarefa")
print("4-Mostrar ultima tarefa")
while True:
    comando = int(input("Digite um comando: "))
    if comando == 1:
        with open('tarefas.txt','a') as arquivo:
            for valor in arquivo:
                print(valor)
    elif comando == 2:
        nova_trefa()
    elif comando == 3:
        remover_tarefa()
    elif comando == 4:
        print(atividades[-1])
        atividades.pop()
        print(atividades[-1])
    else:
        print("Comando inválido")