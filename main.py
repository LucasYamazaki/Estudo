atividades = []
def nova_trefa():
    nova_tarefa = input("Digite uma tarefa: ").strip()
    atividades.append(nova_tarefa)
def remover_tarefa():
    selecionar = input("Digite o nome da tarefa que quer remover: ").strip()
    try:
        atividades.remove(selecionar)
        print("Atividade removida.")
    except Exception:
        print("Atividade não encontrada.")

print("---Menu---")
print("1-Ver tarefas")
print("2-Adicionar tarefa")
print("3-Remover tarefa")
print("4-Mostrar ultima tarefa")
while True:
    comando = int(input("Digite um comando: "))
    if comando == 1:
        print(atividades)
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