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

# gerar id 

def gerar_id(tarefas):
    if tarefas:
        return tarefas[-1][id] + 1


# Adicionar tarefas

def adicionar_tarefas(tarefas):    
    print("Inclua a tarefa")
    titulo = input("Titulo: ")
    descricao = input("Descrição: ")

    tarefa = {
        'id': gerar_id(tarefas),
        'titulo': titulo,
        'descricao': descricao,
        'concluida': False

    }
     
    tarefas.append(tarefa)  
    salvar_tarefas(tarefas)
    print("Tarefa inserida com sucesso!")

# função de concluir tarefas codigo melhorado pelo chat gpt


def concluir_tarefa(tarefas):
    for tarefa in tarefas:
        print(f"ID: {tarefa['id']}, Titulo: {tarefa['titulo']}")

    while True:
    
        id_escolhido = input("Digite o ID: ")
    
        if not id_escolhido.isdigit():
            print("Digite apenas números.")
            continue
    
        id_escolhido = int(id_escolhido)
    
        encontrou = False
    
        for tarefa in tarefas:
    
            if tarefa["id"] == id_escolhido:
    
                encontrou = True
    
                if tarefa["concluida"]:
                    print("Essa tarefa já está concluída.")
                else:
                    tarefa["concluida"] = True
                    salvar_tarefas(tarefas)
                    print("Concluída com sucesso!")
    
                break
    
        if encontrou:
            break
    
        print("ID não encontrado.")


    
# meu codigo para analisar futuramente    
    # while True:
        # id_escolhido = input("Digite o ID da tarefa a concluir: ")
        # # int() converte o texto digitado em número, para bater com o tipo do 'id' no JSON
    
        # # Validar se digitou um numero de ID valido
    
        # if not id_escolhido.isdigit():
                # print("Isso não é um número valido! Digite novamente")
                # continue 
        
        # # tranformar o valor digitado em int 
    
        # id_escolhido = int(id_escolhido)   

        # # validar se o id existe
        
        # #for tarefa in tarefas:
        # #    if tarefa['id'] == id_escolhido: 
        # #        break
        # #    else:
        # #        print("ID não encontrado, tente novamente.") 
     
    
        # for tarefa in tarefas:
            # if tarefa['id'] == id_escolhido:
                # if tarefa['concluida'] == True:
                    # print(f"A tarefa de ID: {id_escolhido} ja estava com status concluida")

                # elif id_escolhido != tarefa['id']:
                    # print("ID Não enonrtado")
                    # continue  
                                    
                # else:
                    # tarefa['concluida'] = True
                    # print("Tarefa concluída com sucesso!")   
                                
            
                # # aqui você está alterando o próprio dicionário que está dentro da lista,
                # # não uma cópia; é por isso que não precisa reatribuir tarefas depois
                
                # # o break existe porque, uma vez achado o ID certo, não há motivo
                # # para continuar percorrendo o resto da lista
        # break 
        # salvar_tarefas(tarefas)
    
              
        
        


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