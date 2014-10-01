__author__ = 'AndreMart'
#Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.
aux = 2 ** 1000000
aux = str(aux)
print(len(aux)," caracteres ")