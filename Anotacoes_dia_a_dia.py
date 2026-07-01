# modulos
# Pacotes que podem estar ou não no Python
# Estão? = Importa
# Não Estão = Instala com gerenciador de dependencias . Geralmente é o PIP

# Aula 11 = Dicionarios

# Dicinarios nada mais é que Objetos em outras linguagens de programação

# Array = []
# Tupla = ()
# Dicionario = {}

aluno = {
    "nome": "Rodolfo",
    "Profissão": "Colecionador de fracassos",
    "idade": "32"
}

# Sintaxy "Nome_da_chave": "Valor_da_chave"

print(aluno["nome"])
print("Seu nome é {}, e sua profissão é {}".format(aluno["nome"], aluno["Profissão"]))

# atribuição e atualização 

aluno["nota"] = 12
aluno["nome"] = "Rodolfo Gaspar"

print(aluno)

# remocão de informações 

del aluno["idade"]

print(aluno)

#conjuntos em outras linguagens é conhecida como set

def nova_nota(aluno):
    aluno["prova_a"] = int(input("Digite a nota da prova a"))

