import time
cont = 0
a2 = 0
maior = 0
menor = 0

while cont<1:
    a2 = int(input("Insira um valor inteiro: "))
    menor = a2
    cont+=1

while cont<10:
    a2 = int(input("Insira um valor inteiro: "))
    if a2 > menor:
        maior = a2
    else:
        menor = a2
    cont+=1

print ("O maior número é:",maior,"\nO menor número é:", menor)