__author__ = 'AndreMart'
#Solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar.
preco = float(input("Insira o preço de sua mercadoria                      ... "))
desconto = float(input("Insira o desconto  em porcentage de sua mercadoria ... "))
desconto = desconto * 0.01
desconto = desconto * preco
preco = preco - desconto
print("O seu desconto é %f" %desconto, " o total a pagar é %f" %preco)