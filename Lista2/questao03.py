__author__ = 'AndreMart'
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
# trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do
# estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que
# você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver,
# gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário
# mostrar tais variáveis com o conteúdo ZERO.
peso = float(input(" Digite a quantidade em peso do seu pescado "))
if peso <= 50:
    print(" Você não vai pagar nada de multa ")
    multa = "ZERO"
    excesso = "ZERO"
elif peso > 50:
    excesso = peso - 50
    multa = excesso * 4.00
print(" Você pescou %6.2f" %peso, " Você teve o excesso de", excesso, "Você vai pagar multa de", multa)



