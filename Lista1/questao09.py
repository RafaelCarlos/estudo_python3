__author__ = 'AndreMart'
#9) Escreva um programa que pergunte a quantidade de km percorridos por um
# carro alugado pelo usuário, assim como a quantidade de dias pelos quais o
# carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa
# R$ 60,00 por dia e R$ 0,15 por km rodado.
kmRodado = float(input("Qual foi a quantidade de Km percorrido "))
dias = float(input("qual foi a quantidade de dias que você ficou com o carro "))
dias = dias * 60
kmRodado = kmRodado * 0.15
print("O total a pagar é ", dias + kmRodado)