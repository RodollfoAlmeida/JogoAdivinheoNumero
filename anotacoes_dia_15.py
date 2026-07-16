# classe -> objeto
# Classe é o molde do objeto 
# intanio um objeto (criar um objeto)
    
class pessoa:    
    # caracteristicas e ações do objeto
    # nome = carateristicas => propriedades, atributos
    # apresentar = ação => metodo    

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentacao(self):
        print(f"Ola, meu nome é {self.nome} e eu tenho {self.idade} anos")
    
    # idade aumenta em 1

    def aniversario(self):
        self.idade += 1
        print(f"fiz aniversario, agora tenho {self.idade} anos")
        

# pessoa => jose, 2
# self => os valores no objeto
# variavel = Clase(atributos1, atributos2)
pessoa1 = pessoa("jose", 2)

# metodos = função do objeto 
pessoa1.apresentacao()
pessoa1.aniversario()
pessoa1.aniversario()


class retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura
        

ret = retangulo(14, 55)
ret2 = retangulo(12, 45)

print(ret2.area())
print(ret.area())
        