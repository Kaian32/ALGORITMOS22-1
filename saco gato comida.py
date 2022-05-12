saco = float(input("Qual o peso do saco de ração em quilos?\n"))
grac = float(input("Qual a quantidade em gramas que você coloca para cada gato?\n"))

resto = saco-(((grac*2)*5)/1000)

print("Após 5 dias, vai sobrar",resto,"quilos no saco de ração.")