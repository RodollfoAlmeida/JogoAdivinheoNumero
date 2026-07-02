# TRatamento de erros e exceções
# Criar programas que precisam estar a prova de falhas

# funções try except else finally

try: 
    arquivo = open("dados.txt")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: o arquivo não existe")
else:
    print("Arquivo Lido!")
    print(conteudo)
finally:
    print("operação finalizada")
    if 'arquivo' in locals():
         arquivo.close()
         print("Arquivo Fechado!")


while True:
       try:
           numero = int(input("Digite um numero "))
           resultado = 100 / numero
       except ValueError:
           print("Entrada invalida, tente novamente")
       except ZeroDivisionError:
            print("divisião por zero, tente novamente")
       else:
            print("O resultado de 100 / {} é igual a {}".format(numero, resultado))
            break
       

        