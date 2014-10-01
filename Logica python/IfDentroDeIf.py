__author__ = 'AndreMart'
#Considere a empresa de telefonia thau abaixo de 200 minutos a empresa cobra 0,20 centavos o minuto
#entre 200 e 400 o preço cobrado por cada minuto é 0,18 acima de 400 minutos o preço por minuto é 0,15 centavos
# calcule sua conta de telefone
minutos = float(input("Digite a quantidade de minutos que você gastou"))
if minutos <= 400:
    if minutos <= 200:
        valorConta = minutos * 0.20
    if minutos > 200 and minutos <= 400:
       valorConta = minutos * 0.18
else:
    if minutos > 400 and minutos <= 800:
        valorConta = minutos * 0.15
    else:
        valorConta = minutos * 0.08
print("o valor de sua conta é R$ %6.2f" %valorConta)
