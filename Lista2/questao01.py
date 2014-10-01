__author__ = 'AndreMart'
# Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem
# ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo
# é: equilátero, isósceles ou escaleno.
ladoInferior = int(input(" Digite o primeiro lado do triangulo "))
ladoEsquerdo = int(input(" Digite o segundo lado do triangulo "))
ladoDireito = int(input(" Digite o terceiro lado do triangulo "))
if ladoInferior == ladoEsquerdo and ladoEsquerdo == ladoDireito:
    print(" O seu triangulo é equilatero ")
elif ladoInferior == ladoEsquerdo or ladoInferior == ladoDireito or ladoDireito == ladoEsquerdo:
    print(" O seu triangulo é isóceles ")
elif ladoInferior + ladoEsquerdo < ladoDireito or ladoInferior + ladoDireito < ladoEsquerdo or ladoEsquerdo + ladoDireito < ladoInferior:
    print(" O seu triangulo é escaleno ")
else:
    print(" não é um triangulo ")
