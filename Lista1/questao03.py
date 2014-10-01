__author__ = 'AndreMart'
#Escreva um programa que leia a quantidade de dias, horas, minutos
# e segundos do usuário. Calcule o total em segundos.
dias = int(input("Digite a quantidade de dias         ... "))
horas = int(input("Digite a quantidade de horas       ... "))
segundos = int(input("Digite a quantidade de segundos ... "))
dias = ((dias * 24)*60) * 60
horas = (horas * 60)*60
segundos = (horas) + (dias) + (segundos)
print(segundos)
