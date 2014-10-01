__author__ = 'AndreMart'
#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros
# fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
# calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
qtdFumadoPorDia = int(input("Digite a quantidade de cigarros fumados por dia "))
anosDeFumo = int(input("Quantos anos você já fumou "))
qtdFumadoPorDia = ((((anosDeFumo * 365) * qtdFumadoPorDia) * 10) / 60) / 24

print("Os seus dias estão acabando você já perdeu %d" %qtdFumadoPorDia, " Dias")