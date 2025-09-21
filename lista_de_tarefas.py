lista_de_tarefas = []
NOME_ARQUIVO = "tarefas.txt"

# Tenta carregar as tarefas do arquivo, se ele existir
try:
    with open(NOME_ARQUIVO, "r") as arquivo:
        for linha in arquivo:
            lista_de_tarefas.append(linha.strip())
    print("Tarefas carregadas com sucesso!")
except FileNotFoundError:
    print("Nenhum arquivo de tarefas encontrado. Começando com uma lista vazia.")

while True:
    print("\n--- Lista de Tarefas ---")
    print("O que você gostaria de fazer?")
    print("1. Adicionar uma tarefa")
    print("2. Excluir uma tarefa")
    print("3. Ver todas as tarefas")
    print("4. Sair do programa")

    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")
        lista_de_tarefas.append(tarefa)
        print(f'Tarefa "{tarefa}" adicionada com sucesso!')

    elif opcao == "2":
        if not lista_de_tarefas:
            print("Não há tarefas para excluir.")
        else:
            print("\n--- Tarefas para Excluir ---")
            for i, tarefa in enumerate(lista_de_tarefas, 1):
                print(f"{i}. {tarefa}")
            
            try:
                num_tarefa = int(input("Digite o número da tarefa para excluir: "))
                
                if 0 < num_tarefa <= len(lista_de_tarefas):
                    tarefa_removida = lista_de_tarefas.pop(num_tarefa - 1)
                    print(f'Tarefa "{tarefa_removida}" excluída com sucesso!')
                else:
                    print("Número de tarefa inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
                
    elif opcao == "3":
        if not lista_de_tarefas:
            print("Nenhuma tarefa para mostrar. Adicione algumas!")
        else:
            print("\n--- Suas Tarefas ---")
            for i, tarefa in enumerate(lista_de_tarefas, 1):
                print(f"{i}. {tarefa}")
                
    elif opcao == "4":
        print("Salvando as tarefas...")
        with open(NOME_ARQUIVO, "w") as arquivo:
            for tarefa in lista_de_tarefas:
                arquivo.write(tarefa + "\n")
        print("Tarefas salvas. Saindo do programa. Até mais!")
        break
        
    else:
        print("Opção inválida. Tente novamente.")