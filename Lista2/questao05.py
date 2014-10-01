__author__ = 'AndreMart'
#Faça um Programa que leia três números e mostre o maior deles e o menor deles.
n1 = int(input("Digite no numero 1 "))
n2 = int(input("Digite o numero 2 "))
n3 = int(input("Digite o numero 3 "))

if n1 > n2 and n1 > n3:
    print("o maior é o n1")
    if n2 < n3:
        print("o menor é o n2 e o meio é n3")
    else: print("o menor é o n3 e o meio é n2")
elif n2 > n3 and n2 > n1:
    print("o maior é o numero n2")
    if n3 < n1:
        print("o menor é o n3 e o meio é o n1 ")
    else: print("o menor é o n1 e o meio é o n3")
elif n3 > n1 and n3 > n2:
    print("o maior é o numero n3 ")
    if n1 < n2:
        print("o menor é o n1 e o meio é n2")
    else: print("o menor é o n2 e o meio é n1")