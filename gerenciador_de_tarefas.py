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
        print(f"ID: {tarefa['id']}, Titulo: {tarefa['titulo']}")
    
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
            break
        if opcao == '2':
            listar_tarefas(tarefas)



if __name__ == '__main__':
    main()