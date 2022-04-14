# trocando valores durente a execução do código

# os inputs são a e b
a = int( input("Insira o valor de A:") )
print ("\n")
b = int( input("Insira o valor de B:") )

# saída dos valores
print ("\n")
print ("A vale:", a, "e B vale:", b, "\n")

# etapa dos cálculos
c = a
d = b

b = c
a = d

# saída dos valores agora já calculados
print ("Agora, A vale:", a, "e B vale:", b, "\n")

# soma de a com b, agora já invertidos
z = a+b

# saída da soma dos dois valores
print ("A soma destes valores equivale a: ", z)

#se for maior que 50, falar parabéns
if (z>50):
    print("PARABÉNS! A soma de seus números foi maior que 50!")
else:
    print("PUTZ! A soma deu menos que 50!")
# testando a escape bar
print ("já dizia seu tonho: \"tem que colocar barra pra esquerda pra colocar aspas duplas\"")




# só para dar 32 linhas mesmo lol