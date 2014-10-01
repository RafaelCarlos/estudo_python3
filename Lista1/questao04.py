__author__ = 'AndreMart'
#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário
# e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
salario = float(input("Digite o valor do salario para ser calculado, "))
aumento = float(input("Digite o valor da porcentagem (%) do aumento, "))
aumento = ((0.01 * aumento) * salario) + salario
print("O seu novo salário é " , aumento)