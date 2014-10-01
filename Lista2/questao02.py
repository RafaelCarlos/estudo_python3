__author__ = 'AndreMart'
#Determine se um ano é bissexto. Verifique no Google como fazer isso...
#condição 01: Ser divisivel por 4 e não finalizar em 00
#condição 02:  Ser divisivel por 4 finalizar em 00 e ser divisivel por 400
ano = int(input("Digite o ano para ser conferido se é bicesto ou não "))
anoCondicaoUm = False
anoCondicaoDois = False

# Código para pegar os dois ultimos caracteres
aux = str(ano)
aux = aux[-2::]
aux = int(aux)

if ano % 4 == 0 and aux != 00:
    print("%d é bicesto" %ano)
elif ano % 4 == 0 and ano % 400 == 0 and aux == 00:
    print("%d é bicesto" %ano)
else:
    print("não é bicesto")
