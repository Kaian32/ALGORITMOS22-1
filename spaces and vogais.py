frase = list(input("Por favor, insira a frase que deseja:\n"))
spaces = frase.count(" ")
a = frase.count("a")
e = frase.count("e")
i = frase.count("i")
o = frase.count("o")
u = frase.count("u")
vogais = a+e+i+o+u
print("A frase possui",spaces,"spaces e",vogais,"vogais.")