# Gerenciador de Tarefas avançado
import os
import json
from datetime import datetime

# função para caregar tarefas

def carregar_tarefas():
    if os.path.exists('tarefas.json'):
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    return []    

# listar as tarefas
def listar_tarefas(tarefas):
    print("Tarefas:")
    for tarefa in tarefas:
        status = "Concluida" if tarefa['concluida'] else "Pendente"
        print(f"ID: {tarefa['id']}, Titulo: {tarefa['titulo']}, Status: {status}")


# Escreve no arquivo e salva Tarefas 

def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
            json.dump(tarefas, arquivo, indent=4)


# Adicionar tarefas

def adicionar_tarefas(tarefas):    
    print("Inclua a tarefa")
    titulo = input("Titulo: ")
    descricao = input("Descrição: ")

    tarefa = {
        'id': len(tarefas) + 1,
        'titulo': titulo,
        'descricao': descricao,
        'status': False

    }
     
    tarefas.append(tarefa)  
    salvar_tarefas(tarefas)
    print("Tarefa inserida com sucesso!")

# função de concluir tarefas

def concluir_tarefa(tarefas):
    for tarefa in tarefas:
        print(f"ID: {tarefa['id']}, Titulo: {tarefa['titulo']}")

    id_escolhido = int(input("Digite o ID da tarefa a concluir: "))
    # int() converte o texto digitado em número, para bater com o tipo do 'id' no JSON

    for tarefa in tarefas:
        if tarefa['id'] == id_escolhido:
            tarefa['concluida'] = True
            # aqui você está alterando o próprio dicionário que está dentro da lista,
            # não uma cópia; é por isso que não precisa reatribuir tarefas depois
            break
            # o break existe porque, uma vez achado o ID certo, não há motivo
            # para continuar percorrendo o resto da lista

    salvar_tarefas(tarefas)
    print("Tarefa concluída com sucesso!")
  

    
# Menu de Tarefas

def menu():
    print("=== GRENCIADOR DE TAREFAS ===")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. concluir Tarefa")
    print("4. Remover Tarefa")
    print("5. Sair")
    return input("Escolha uma opção: ")

# função central do meu sistema que sera um loop das ações 

def main():
    tarefas = carregar_tarefas()
    while True:
        opcao = menu()
        if opcao == '1':
            adicionar_tarefas(tarefas)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            concluir_tarefa(tarefas)
        elif opcao == '4':
            excluir_tarefa(tarefas)
        elif opcao == '5':
            print("Encerrando o programa...")
            break
        else:
            print("Opção Invalida!")



if __name__ == '__main__':
    main()