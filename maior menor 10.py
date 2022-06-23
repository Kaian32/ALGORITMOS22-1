import time
cont = 0
a2 = 0
maior = 0
menor = 0

for cont in range(1):
    a2 = int(input("Insira um valor inteiro: "))
    menor = a2
    

for cont in range(10):
    a2 = int(input("Insira um valor inteiro: "))
    if a2 > menor:
        if a2 > maior:
            maior = a2
    elif a2 < menor:
        menor = a2
    
print ("O maior número é:",maior,"\nO menor número é:", menor)