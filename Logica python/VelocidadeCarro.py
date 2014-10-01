__author__ = 'AndreMart'
#Pergunte a velocidade de um carro supondo um valor inteiro, caso ele ultrapasse 110km/h exiba uma mensagem dizendo
# que o usuário foi multado. neste caso, exiba o valor da multa, cobrando R$ 5,00 por km acima de 110
velocidade = int(input("Digite a velcidade que você está "))
if(velocidade > 110):
    multa = (velocidade - 110) * 5
    print("Você foi multado em %d" %multa, "Agora é pagar não é")
else:
    print("Você não foi multado")
