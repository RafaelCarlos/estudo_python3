__author__ = 'AndreMart'
#programa com entrada de dados
a = int(input("Digite o primeiro numero"))
b = int(input("Digite o Segundo numero"))
print(a + b)
a = float(input("Digite o primeiro numero"))
b = float(input("Digite o Segundo numero"))
print(a + b)

class A:
    nome = "Mauro"

class B(A):
    pass

def funcao(**a):
    return a

class C:

    def __init__(self, a, b):
        self.idade = 1


class D(C, A):
    pass

z = D()
print(z.nome)
print(z.sobrenome)
